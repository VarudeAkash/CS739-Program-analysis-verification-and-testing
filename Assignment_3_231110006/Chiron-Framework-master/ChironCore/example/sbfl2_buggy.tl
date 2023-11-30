penup
if :y >0 [
	if :x > 0[
		if :y > :x[
			if :z<0[
				left 20
				forward 100
			]
			else
			[
				right 70
				forward 120
			]
		]
		else[
			if :z>0[
				right 60
				forward 100
			]
			else
			[
				left 65
				forward 200
			]
		]
	]
	else[
		if :y > :x[
			if :z>0[
				forward 150
			]
			else
			[
				forward 240
			]
		]
		else[
			if :z>0[
				forward 10
			]
			else
			[
				forward 130
			]
		]
	]
]
else[
	if :y > :x[
		if :z<0[
			left 10
		]
		else
		[
			right 20
		]
	]
	else[
		if :z>0[
			forward 10
			left 45
		]
		else
		[
			forward 20
			right 30
		]
	]
]