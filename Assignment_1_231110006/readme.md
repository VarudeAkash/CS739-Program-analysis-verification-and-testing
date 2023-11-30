Instructions to run fuzzer on my created test files(.tl extension files) :
	-I have created 5 test files. These are present in Test folder under kachua core folder
	-I have used only two parameters :x and :y in all of test.tl files
	-I have used parameter values in kachua commands (e.g.   forward :x/2
								 left :y/3 etc)
		hence to make sure kachua is runnig in visible whiteboard please use :x and :y values within range (-500 to 500)
		However if you want to use my mutation on your test files(.tl files) you can use any number of parameters and 
		any values(not limited to any specific range) you want.


for running fuzzer, goto kachuaCore in command promp and run commands mentioned below:

my system runs fuzzer using the command->
for e.g.
	kachua.py -t 60 --fuzz Tests/test2.tl -d{':x':-10,':y':100}
or 
	./kachua.py -t 60 --fuzz Tests/test2.tl -d{':x':-10,':y':100}

you can write python if your system required so:
for e.g.
	python3 kachua.py -t 60 --fuzz Tests/test2.tl -d{':x':-10,':y':100}
or
	python3 ./kachua.py -t 60 --fuzz Tests/test2.tl -d{':x':-10,':y':100}