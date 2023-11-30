I have used only two parameters :x and :y in all of test.tl files

for running fuzzer, goto kachuaCore in command promp and run commands mentioned below:

my system runs fuzzer using the command->
for e.g.
	kachua.py -t 60 --fuzz Tests/test2.tl -d{'x:':-10,':y':0}
or 
	./kachua.py -t 60 --fuzz Tests/test2.tl -d{'x:':-10,':y':0}

you can write python if your system required so:
for e.g.
	python3 kachua.py -t 60 --fuzz Tests/test2.tl -d{'x:':-10,':y':0}
or
	python3 ./kachua.py -t 60 --fuzz Tests/test2.tl -d{'x:':-10,':y':0}