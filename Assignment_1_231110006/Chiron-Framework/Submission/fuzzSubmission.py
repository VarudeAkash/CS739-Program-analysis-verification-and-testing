from kast import kachuaAST
import sys
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')
import numpy as np
import random

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return any(item for item in curr_metric if item not in total_metric)

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        unique_elements = set(curr_metric) | set(total_metric)
        total_metric = list(unique_elements)
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        max_range=500
        min_range=-500
        #num_keys_to_mutate = random.randint(1,2)        # Randomly selecting the number of keys to mutate (0, 1, or 2)        
        data_dict=input_data.data                       # Randomly selecting which keys to mutate
        keys_list=list(data_dict.keys())
        num_keys_to_mutate=random.randint(1,len(keys_list))
        keys_to_mutate = random.sample(keys_list, num_keys_to_mutate)
        for key in keys_to_mutate:
            value = data_dict[key]                      #getting value of chosen key
            mutation_type = random.randint(1, 5)        #randomly selecting which mutation to perform
            if mutation_type==1:                        #randomly choosing addition or subtraction of random number
                operation = random.choice(["+", "-"])
                mutation_value = np.random.rand()
                range1=np.random.rand()*3
                range2=np.random.rand()*3
                if operation == "+":
                    value += mutation_value*range1
                else:
                    value -= mutation_value*range2
            elif mutation_type==2:                      #Changing sign of a number
                value= -value
            elif mutation_type==3:                      #making number within certain range
                mutation_range1=np.random.rand()*500
                mutation_range2=np.random.rand()*500
                random_value = random.uniform(-mutation_range1, mutation_range2)
                mutated_value = value + random_value
                value=mutated_value
            elif mutation_type==4:
                zeros_number=random.randint(0, 1)       #choosing whether to make key to zero or not
                if(zeros_number==1):
                    value=0
            elif mutation_type==5:                      #performing bitwise XOR
                bitmask  = random.randint(0, 0b11111111)  #creating a random bitmask of bit length 8 
                value = int(value)
                mutated_number = value ^ bitmask
                value=mutated_number
            input_data.data[key] = value
        return input_data


# Reuse code and imports from
# earlier submissions (if any).
