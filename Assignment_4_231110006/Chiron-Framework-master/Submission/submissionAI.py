import copy
import math

from typing import overload
import json
import sys
sys.path.insert(0, "../ChironCore/")

import cfg.ChironCFG as cfgK
import cfg.cfgBuilder as cfgB
from lattice import  *
import ChironAST.ChironAST as ChironAST
import abstractInterpretation as AI

import numpy as np
from xmlrpc.client import MAXINT, MININT
from collections import namedtuple


'''
    Class for interval domain
'''
# global ini_dict
class IntervalDomain(Lattice):

    '''Initialize abstract value'''
    def __init__(self, L, R):
        self.L = L
        self.R = R

    '''To check whether abstract value is bot or not'''
    def isBot(self):
        return self.data is None


    '''To display abstract values'''
    def __str__(self):
        return f"[{self.L}, {self.R}]"
        # pass

    
    '''To check whether abstract value is Top or not'''
    def isTop(self):
        return self.data == (int('-inf'), int('inf'))

    
    '''Implement the join operator'''
    def join(self, other):
        if self.isTop() or other.isTop(): # if either of the element is top,then their join is top element
            return IntervalDomain((int('-inf'), int('inf')))  # Top element
        return IntervalDomain((min(self.L, other.L), max(self.R, other.R))) # finding the union of the intervals

    '''Implement the meet operator'''
    def meet(self, other):
        if self.isBot() or other.isBot():           # if any one of the element is bottom then their meet is also bottom
            return IntervalDomain(None)             # Bottom element
        return IntervalDomain((max(self.L, other.L), min(self.R, other.R))) #finding the intersection of the intervals


    '''partial order with the other abstract value'''
    def __le__(self, other):
        if self.is_top() or other.is_bot():
            return True
        elif self.is_bot() or other.is_top():
            return False
        else:
            return self.R <= other.L


    '''equality check with other abstract value'''
    def __eq__(self, other):
        return self.L == other.L and self.R == other.R
        # pass


    '''
        Add here required abstract transformers
    '''
    def __lt__(self, other):
        # Less than check
        return self.upper < other.lower

    def __gt__(self, other):
        # Greater than check
        if self.is_bot() or other.is_top():
            return False
        elif self.is_top() or other.is_bot():
            return True
        else:
            return self.L > other.R

    def __ge__(self, other):
        
        if self.is_bot() or other.is_top():
            return False
        elif self.is_top() or other.is_bot():
            return True
        else:
            return self.L >= other.L

    
    def __sub__(self, other):
        if self.is_bot() or other.is_bot():
            return None
        else:
            return IntervalDomain(self.L - other.R, self.R - other.L)
    def __add__(self, other):
        if self.is_bot() or other.is_bot():
            return None
        else:
            return IntervalDomain(self.L + other.L, self.R + other.R)
    pass

assgn_dict = {}


class IntervalTransferFunction(TransferFunction):
    def __init__(self):
        pass

    def transferFunction(self, currBBIN, currBB):
        '''
            Transfer function for basic block 'currBB'
            args: In val for currBB, currBB
            Returns newly calculated values in a form of list

            This is the transfer function you write for Abstract Interpretation.
        '''
        outVal = []
        global theta
        current_out = copy.deepcopy(currBBIN)
        # print(current_out)
        if (currBB.__str__() != 'END'):
            if (type(currBB.instrlist[0][0]) == ChironAST.ConditionCommand):
                if (str(currBB.instrlist[0][0]) != 'False'):
                    l = len(currBB.instrlist[0][0].__str__())
                    var, op, val = str.split(currBB.instrlist[0][0].__str__()[1:l - 1])

                    if(var in list(assgn_dict.keys())):
                        value1 = assgn_dict[var]
                    value2 = int(val)
                    if(op == '<'):
                        true_range = IntervalDomain(MININT , value2-1)
                        false_range = IntervalDomain(value2 ,  MAXINT)
                    if(op == '>'):
                        true_range = IntervalDomain(value2+1 , MAXINT)
                        false_range = IntervalDomain(MININT ,  value2)
                    if(op == '<='):
                        true_range = IntervalDomain(MININT , value2)
                        false_range = IntervalDomain(value2+1 ,  MAXINT)
                    if(op == '>='):
                        true_range = IntervalDomain(value2 ,  MAXINT)
                        false_range = IntervalDomain(MININT ,  value2-1)
                    if(op == '=='):
                        true_range = IntervalDomain(value2 , value2)
                        false_range = IntervalDomain(MININT ,  MAXINT)
                        # false_range.remove(value2)
                    final_true_range = IntervalDomain(max(true_range.L,value1.L) ,  min(true_range.R , value1.R))
                    final_false_range = IntervalDomain(max(false_range.L,value1.L) ,  min(false_range.R , value1.R))

                    [true_range, false_range] = [final_true_range,final_false_range]
                    current_out1 = copy.deepcopy(current_out)
                    current_out2 = copy.deepcopy(current_out)
                    current_out1[var] =  IntervalDomain(true_range.L,  true_range.R)
                    current_out2[var] =  IntervalDomain(false_range.L,  false_range.R)
                    outVal = [current_out1, current_out2]
                    return outVal
                else:
                    outVal = [current_out, current_out]
                    return outVal
            elif (type(currBB.instrlist[0][0]) == ChironAST.MoveCommand):
                flag = 0
                split_list = str.split(str(currBB.instrlist[0][0]))
                if (type(currBB.instrlist[0][0].expr) == ChironAST.Num):
                    mov = IntervalDomain(int(currBB.instrlist[0][0].expr.__str__()),
                           int(currBB.instrlist[0][0].expr.__str__()))
                elif (str(currBB.instrlist[0][0].expr) in assgn_dict.keys()):
                    mov = assgn_dict[split_list[1]]
                else:
                    assgn_dict[str(currBB.instrlist[0][0].expr)] = [ int('-inf'),int('inf')]
                    mov = (assgn_dict[split_list[1]])

                if (split_list[0] == "left"):
                    for j in range(len(current_out['theta'])):
                        current_out['theta'][j] += int(mov.L)
                if (split_list[0] == "right"):
                    for j in range(len(current_out['theta'])):
                        current_out['theta'][j] -= int(mov.L)
                if (flag == 0):
                    
                    if (split_list[0] == "backward"):
                        X_L = []
                        X_R = []
                        Y_L = []
                        Y_R = []
                        for j in range(len(current_out['theta'])):
                            temp=current_out['X'].L - int(mov.L) * int(math.cos(current_out['theta'][j] * math.pi / 180))
                            X_L.append(temp)
                            temp=current_out['X'].R - int(mov.R) * int(math.cos(current_out['theta'][j] * math.pi / 180))
                            X_R.append(temp)
                            temp=current_out['Y'].L - int(mov.L) * int(math.sin(current_out['theta'][j] * math.pi / 180))
                            Y_L.append(temp)
                            temp=current_out['Y'].R - int(mov.R) * int(math.sin(current_out['theta'][j] * math.pi / 180))
                            Y_R.append(temp)
                        current_out['X'].L = min(X_L)
                        current_out['X'].R = max(X_R)
                        current_out['Y'].L = min(Y_L)
                        current_out['Y'].R = max(Y_R)
                        
                    if (split_list[0] == "forward"):
                        X_L = []
                        X_R = []
                        Y_L = []
                        Y_R = []
                        for j in range(len(current_out['theta'])):
                            temp=current_out['X'].L + int(mov.L) * int(math.cos(current_out['theta'][j] * math.pi / 180))
                            X_L.append(temp)
                            temp=current_out['X'].R + int(mov.R) * int(math.cos(current_out['theta'][j] * math.pi / 180))
                            X_R.append(temp)
                            temp=current_out['Y'].L + int(mov.L) * int(math.sin(current_out['theta'][j] * math.pi / 180))
                            Y_L.append(temp)
                            temp=current_out['Y'].R + int(mov.R) * int(math.sin(current_out['theta'][j] * math.pi / 180))
                            Y_R.append(temp)
                        current_out['X'].L = min(X_L)
                        current_out['X'].R = max(X_R)
                        current_out['Y'].L = min(Y_L)
                        current_out['Y'].R = max(Y_R)      
        outVal = [current_out]
        return outVal

class ForwardAnalysis():
    def __init__(self):
        self.transferFunctionInstance = IntervalTransferFunction()
        self.type = "IntervalTF"
        # pass

    '''
        This function is to initialize in of the basic block currBB
        Returns a dictinary {varName -> abstractValues}
        isStartNode is a flag for stating whether currBB is start basic block or not
    '''
    def initialize(self, currBB, isStartNode):
        val = {}
        global ini_dict
        if(isStartNode):
            val = {'X':IntervalDomain(0, 0), 'Y': IntervalDomain(0, 0), 'theta': [0]}
        return val
  
    #just a dummy equallity check function for dictionary
    def isEqual(self, dA, dB):
        for i in dA.keys():
            if i not in dB.keys():
                return False
            if dA[i] != dB[i]:
                return False
        return True

    '''
        Define the meet operation
        Returns a dictinary {varName -> abstractValues}
    '''
    def meet(self, predList):
        assert isinstance(predList, list)
        #print('predlist\n',predList)
        meetVal = {}
        final_x_left = []
        final_x_right = []
        final_y_left = []
        final_y_right = []
        dir = []
        for i in predList:
            final_x_left.append(i['X'].L)
            final_x_right.append(i['X'].R)
            final_y_left.append(i['Y'].L)
            final_y_right.append(i['Y'].R)
            if i['theta'][0]%360 not in dir:
                dir.append(i['theta'][0]%360)

        meetVal = { 'X': IntervalDomain(min(final_x_left), max(final_x_right)), 'Y': IntervalDomain(min(final_y_left), max(final_y_right)),'theta': dir}
        
        return meetVal

def analyzeUsingAI(irHandler):
    '''
        get the cfg outof IR 
        each basic block consists of single statement
    '''

    file = open("../ChironCore/examples/test3.json","r+")
    
    d = json.loads(file.read())
    
    magarmach_point1 = d['reg'][0]
    magarmach_point2 = d['reg'][1]


    for i in irHandler.ir:
        if('__rep_counter_1' in str(i[0])):
            print("\n\"Kachua can be inside magarmach region. Hence Unsafe")
            sys.exit()
        if(type(i[0]) == ChironAST.AssignmentCommand):
            if(':' in (i[0].rexpr.__str__())):
                print("\n\"Kachua can be inside magarmach region. Hence Unsafe")
                sys.exit()
            assgn_dict[i[0].lvar.__str__()] = IntervalDomain(int(i[0].rexpr.__str__()),  int(i[0].rexpr.__str__()))
            #print('assigning dict ',int(i[0].rexpr.__str__()))

    abstractInterpreter = AI.AbstractInterpreter(irHandler)
    bbIn, bbOut = abstractInterpreter.worklistAlgorithm(irHandler.cfg)
    # print('\nIN Solution:\n\n ',bbIn)
    # print('\nOut Solution:\n\n ',bbOut)
    final_turtle_X_pos = bbOut['END'][0]['X']
    final_turtle_Y_pos = bbOut['END'][0]['Y']

    Chiron_point_1 = [final_turtle_X_pos.L,final_turtle_X_pos.R]
    Chiron_point_2 = [final_turtle_Y_pos.L,final_turtle_Y_pos.R]
    xmin = min(magarmach_point1[0],magarmach_point1[1])
    ymin = min(magarmach_point2[0],magarmach_point2[1])
    xmax = max(magarmach_point1[0],magarmach_point1[1])
    ymax= max(magarmach_point2[0],magarmach_point2[1])

    print("\n Possibility of kachua to halt in the region : X from " , Chiron_point_1[0] ," TO " , Chiron_point_1[1]," and y from ",Chiron_point_2[0]," to ",Chiron_point_2[1])
    print("\n Magarmach region : X from " , magarmach_point1[0] ," TO " , magarmach_point1[1]," and y from ",magarmach_point2[0]," to ",magarmach_point2[1])
    if (xmin<=Chiron_point_1[0]<=xmax or xmax>=Chiron_point_1[1]>=xmin) and (ymin<=Chiron_point_2[0]<=ymax or ymax>=Chiron_point_2[1]>=ymin):
        print("Hence there is overlap between possibile region where kachua stops and magarmach region")
        print("\n\",{VERIFIED} Kachua can be inside magarmach region. Hence Unsafe")
    else:
        print("Hence there is no overlap between possibile region where kachua stops and magarmach region")
        print("\n\"Kachua can't be in magarmach region. Hence kachua is safe")
