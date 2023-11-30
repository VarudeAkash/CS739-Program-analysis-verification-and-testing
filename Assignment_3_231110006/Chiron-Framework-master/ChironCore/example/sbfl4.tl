if :x < 0 [
	if :y > -100[
		if :y < 0[
			if :z < 100[
				right 45
				forward 10
			]
			else
			[
				left 80
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
	if :z>0[
		left 30
		forward 50
	]
	else
	[
		forward 100
	]
]