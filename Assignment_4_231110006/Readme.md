As I have windows, pygraphviz library couldn't be installed, Hence I have commented last 3 lines from cfgBuilder.py program
So, CFG is not stored in image format

All .tl and .json files are stored in chironcore/examples folder.
All .json files contains magarmach region
Any program (.tl files) can be executed by using any magarmach regions(any .json files)
 


To run the program, first goto chironcore folder and run following command:
 	python chiron.py --control_flow -ai examples/test3.tl

To use different magarmach region (which are stored in .json files), just update file name in 'analyzeUsingAI' function
currently test3.json is read by the program. However if want to use another region e.g. test4.json file just update the line as
	    file = open("../ChironCore/examples/test4.json","r+")
