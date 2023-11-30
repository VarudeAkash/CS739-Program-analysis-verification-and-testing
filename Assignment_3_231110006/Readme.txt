I have implemented this assignment on chiron framework
all 5 test programs are stored in chironcore/examples folder along with their output

all test programs are have names in the format
sbfl1.tl	sbfl1_buggy.tl
sbfl2.tl	sbfl2_buggy.tl
sbfl3.tl	sbfl3_buggy.tl
sbfl4.tl	sbfl4_buggy.tl
sbfl5.tl	sbfl5_buggy.tl
sbfl6.tl	sbfl6_buggy.tl

All these .tl test programs have three parameters :x , :y and :z

To run the code: goto chironcore folder in command prompt and run following command
	> chiron.py --SBFL ./example/sbfl1.tl --buggy ./example/sbfl1_buggy.tl -vars '[":x".":y",":z"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True
