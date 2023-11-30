I have Implemented this assignment on kachua version2
All test cases Programs are stored in kachuacore/tests folder

Steps to run this assignment:

	1. Step1: Make Json files for both codes
	   -To make Json file run following command (following is example to make json file for test program 'eqtest4')
		kachua.py -t 10 -se tests/eqtest4.tl -d{':x':5,':y':100} -c{':c1':1,':c2':1}

	   -similarly, make json file for program cotaining unknown variables also

	2. Step2 : Make .kw file
	   -Run following command on any empty .tl file. 
	   	python kachua.py -O filename.tl
	   -This will generate optimized.kw file in kachuacore folder. I have copied it in chironframework/Submission folder and renamed it as eqtest.kw

	3. Step3 : Run symbSubmission.py file
	   -first goto Submission folder and run following command
		symbSubmission.py eqtest.kw -e'["x", "y"]'


By default symbSubmission.py reads testData1.json and testData2.json files. If you want to read different files then just change names of files in checkEq() function
