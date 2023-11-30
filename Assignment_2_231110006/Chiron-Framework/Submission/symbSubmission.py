from cgi import test
from z3 import *
import argparse
import json
import sys

sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))



def checkEq(args,ir):

    file1 = open("../Submission/testData1.json","r+")
    testData1=json.loads(file1.read())
    file1.close()
    testData1 = convertTestData(testData1)
    print(testData1)

    file2 = open("../Submission/testData2.json","r+")
    testData2=json.loads(file2.read())
    file2.close()
    testData2 = convertTestData(testData2)
    print("\n",testData2)

    s = zs.z3Solver()
     
    totalPaths1 = list(testData1.keys())        #get number of paths for 1st program
    totalPaths2 = list(testData2.keys())        #get number of paths for 2nd program
    all_parameters=list(testData1[totalPaths1[0]]['params'].keys())     #extract all parameters including constant parameters
    constParams=list(testData1[totalPaths1[0]]['constparams'])          #extract only constParameters 
    constParams = [element[1:] for element in constParams]              # Constparameters are in the form ':c1' hence making them 'c1' like this

    set1=set(all_parameters)
    set2=set(constParams)
    params=list(set1-set2)                      #extract only parameters (all parameters- constParameters)
    for param in all_parameters:
        s.addSymbVar(param)


    '''#Hardcoded Example just for understanding
    s.addSymbVar('o')
    s.addSymbVar('m')
    tmp="And(Implies(And(x<=42,Not(False)),And(m==x,o==x+c1+c2)),Implies(Not(x<=42),And(m==x,o==x+c2)))"
    s.addConstraint("And(Implies((And(x==5,y==100)),And("+tmp+",And(m==5,o==45))),Implies((And(x==43,y==100)),And("+tmp+",And(m==43,o==65))))")
    print('\n\nassertion : ',s.s.assertions())
    res=s.s.check()
    if str(res)=="sat":
        m = s.s.model()
    print("model printing",m)'''

    #Working on Hole Constraints and Outputs
    HoleList=[]
    for i in totalPaths2:
        HoleTmp=""
        symbExpress=""                  #for entire symbolic expression
        HoleSymbExpress1=""
        #Making No Hole Constraint in correct format
        Cflag=0             #flag to check if there are multiple constraints in one NoHoleProgram path Constraints
        HoleConstraint=""
        #Just to make sure, if constraint is like "x <= 42, Not(False)" Then Making it like "And(x <= 42, Not(False))"
        for k in testData2[i]['constraints'][0]:
            if(k==','):
                temp="And("+testData2[i]['constraints'][0]+")"      #Just to make sure, if constraint is like "x <= 42, Not(False)" Then Making it like "And(x <= 42, Not(False))"
                Cflag=1
        if(Cflag):
            HoleConstraint=HoleConstraint+temp
        else:
            HoleConstraint=HoleConstraint+testData2[i]['constraints'][0]
        #print("\nHole Constraint=",HoleConstraint)

        #making no hole outputs in correct format
        opflag=0                #flag to check multiple outputs re there or not
        HoleOutput=""
        output_keys_hole=list(testData2[i]['symbEnc'].keys())            #get keys of outputs
        New_Output_keys_hole=output_keys_hole.copy()
        for k in range(len(params)):
             New_Output_keys_hole[k]=output_keys_hole[k]+'1' 

        for k in range(len(params)):
            if(k!=len(params)-1):
                HoleOutput=HoleOutput+New_Output_keys_hole[k]+" == "+testData2[i]['symbEnc'][output_keys_hole[k]]+", "        #e.g. making "x == output_value, "
                opflag=1
            else:
                HoleOutput=HoleOutput+New_Output_keys_hole[k]+" == "+testData2[i]['symbEnc'][output_keys_hole[k]]             #if output is last output then just make e.g." y=output_value" i.e. don't append comma 
        if(opflag):
            HoleOutput="And("+HoleOutput+")"                    #if multiple outputs are there then just make its expression as "And(op1,op2,op3)"
        #print("Hole Output=",HoleOutput)
        holeTmp="Implies("+HoleConstraint+","+HoleOutput+")"
        HoleList.append(holeTmp)
    tmp=""
    for i in range(len(HoleList)):
        if(i!=len(HoleList)-1):
            tmp=tmp+HoleList[i]+","
        else:
            tmp=tmp+HoleList[i]
    tmp="And("+tmp+")"
    print("\nEntire tmp = ",tmp)
    #Working on Hole Completed, i.e. temp creation done successfully



    #making no hole outputs in correct format
    noHoleOutputList=[]
    for i in totalPaths1:
        opflag=0                #flag to check multiple outputs re there or not
        NoHoleOutput=""
        output_keys_NoHole=list(testData1[i]['symbEnc'].keys())            #get keys of outputs
        #Creating new dictionary as symbEncValues such that e.g. if y : x + c1 +c2 is there then makeing it y: inputValueofx + c1 +c2
        NoHoleSymbEncValues= testData1[i]['symbEnc'].copy()
        for k in params:
            value=list(NoHoleSymbEncValues[k])
            for c in range(len(value)):
                for p in params:
                    if(value[c]==p):
                        value[c]=str(testData1[i]['params'][p])
            NoHoleSymbEncValues[k]="".join(value)                   #new dictionary is now created e.g. NoHoleSymbEncValues= {'x': '5', 'y': '5 + 40', 'c1': 'c1', 'c2': 'c2'} 
        #Now instead of using  symbEnc which was like {'x': 'x', 'y': 'x + 40', 'c1': 'c1', 'c2': 'c2'} we use NoHoleSymbEncValues= {'x': '5', 'y': '5 + 40', 'c1': 'c1', 'c2': 'c2'}     
        #But output variable name should also be changed e.g. if the output is  And(x==5,y==67) then we want And(x1==5,y1==67). Here x1 and y1 represents output variable names
        New_Output_keys_Nohole=output_keys_NoHole.copy()
        for k in range(len(params)):
            New_Output_keys_Nohole[k]=output_keys_NoHole[k]+'1'     #Changing output variable name
            s.addSymbVar(New_Output_keys_Nohole[k])
        for k in range(len(params)):
            if(k!=len(params)-1):
                NoHoleOutput=NoHoleOutput+New_Output_keys_Nohole[k]+" == "+NoHoleSymbEncValues[output_keys_NoHole[k]]+", "        #e.g. making "x == output_value, "
                opflag=1
            else:
                NoHoleOutput=NoHoleOutput+New_Output_keys_Nohole[k]+" == "+NoHoleSymbEncValues[output_keys_NoHole[k]]             #if output is last output then just make e.g." y=output_value" i.e. don't append comma 
        if(opflag):
            NoHoleOutput="And("+NoHoleOutput+")"                    #if multiple outputs are there then just make its expression as "And(op1,op2,op3)"
        noHoleOutputList.append(NoHoleOutput)
    #print("\n NoHoleOutputList= ",noHoleOutputList)



    #Working on no Hole Inputs
    NoHoleInputList=[]
    for i in totalPaths1:
        Ipflag=0                #flag to check multiple inputs re there or not
        NoHoleInput=""
        InputKeys_NoHole=list(testData1[i]['params'].keys())            #get keys of input
        for k in range(len(params)):
            if(k!=len(params)-1):
                NoHoleInput=NoHoleInput+InputKeys_NoHole[k]+" == "+str(testData1[i]['params'][InputKeys_NoHole[k]])+", "        #e.g. making "x == input, "
                Ipflag=1
            else:
                NoHoleInput=NoHoleInput+InputKeys_NoHole[k]+" == "+str(testData1[i]['params'][InputKeys_NoHole[k]])             #if input is last input then just  don't append comma 
        if(Ipflag):
            NoHoleInput="And("+NoHoleInput+")"                    #if multiple inputs are there then just make its expression as "And(op1,op2,op3)"
        NoHoleInputList.append(NoHoleInput)
    #print("\nNoHoleInputList= ",NoHoleInputList)
    
    z3ImpliesList=[]                #list to store all implications of entire expression which needs to be given to z3 solver
    for i in range(len(totalPaths1)):
        z3implies="Implies("+NoHoleInputList[i]+",And("+tmp+","+noHoleOutputList[i]+"))"
        z3ImpliesList.append(z3implies)
        #print("\nAll Implies of expression",z3implies)

    entireExpression=""
    for i in range(len(z3ImpliesList)):
        if(i!=len(z3ImpliesList)-1):
            entireExpression=entireExpression+z3ImpliesList[i]+","
        else:
            entireExpression=entireExpression+z3ImpliesList[i]
    entireExpression="And("+entireExpression+")"

    #print("\nEntire Expression",entireExpression)

    s.addConstraint(entireExpression)
    print('\n\nassertion : ',s.s.assertions())
    res=s.s.check()
    if str(res)=="sat":
        m = s.s.model()
    print("model printing",m)
    


if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
