if :y >0 [
	if :x > 100[
		if :x > 200[
			if :z < 0[
				left 30
				forward 10
			]
			else
			[
				left 40
				forward 60
			]
		]
		else[
			if :z>0[
				right 40
				forward 50
			]
			else
			[
				forward 200
			]
		]
	]
]
else[
	left 30
	forward 100
]