if :y >0 [
	if :x > 100[
		if :x > 200[
			if :z < 0[
				right 45
				forward 10
			]
			else
			[
				left 20
				forward 60
			]
		]
		else[
			if :z>0[
				left 50
				forward 50
			]
			else
			[
				forward 100
			]
		]
	]
]
else[
	left 30
	forward 50
]