forward 100
right 45
:x = 4
:i=1
repeat :x[
	if (:i==0)[
	penup
	:i=1
	]
	else[
	pendown
	:i=0
	]	
	forward 100
	right 90
	]
