penup
if :x < :y [
	if :y > -100[
		forward 100
	]
	else[
		if :z>0[
			left 50
			forward 300
		]
		else
		[
			forward 100
		]
	]
]
else[
	if :z > :y[
		left 60
		forward 150
	]
	else
	[
		forward 100
	]
]