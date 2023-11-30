:a = 50
:b = 20 
if :b <= 100[
	left 50
	forward 60
	if :a<50[
		forward 30
	]
	else[
		right 60
	]
	forward 20
]
else[
	if :a>0 [
		backward 20
	]
	else[
		forward 50
		left 60
	]
	forward 30
]