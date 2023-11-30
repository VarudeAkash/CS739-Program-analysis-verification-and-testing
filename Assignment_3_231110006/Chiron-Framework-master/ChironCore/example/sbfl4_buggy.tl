if :x < 0 [
	if :y > -100[
		if :y < 0[
			if :z < 100[
				right 45
				forward 100
			]
			else
			[
				left 80
				forward 260
			]
		]
		else[
			if :z>0[
				left 50
				forward 50
			]
			else
			[
				left 100
			]
		]
	]
]
else[
	if :z>0[
		right 30
		forward 50
	]
	else
	[
		forward 200
	]
]