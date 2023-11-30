penup
if :y >0 [
	if :x > 0[
		if :y > :x[
			if :z<0[
				left 50
				forward 100
			]
			else
			[
				right 50
				forward 120
			]
		]
		else[
			if :z>0[
				right 90
				forward 100
			]
			else
			[
				left 45
				forward 200
			]
		]
	]
	else[
		if :y > :x[
			if :z>0[
				forward 100
			]
			else
			[
				forward 200
			]
		]
		else[
			if :z>0[
				forward 150
			]
			else
			[
				forward 230
			]
		]
	]
]
else[
	if :y > :x[
		if :z<0[
			left 100
		]
		else
		[
			right 120
		]
	]
	else[
		if :z>0[
			forward 30
			left 45
		]
		else
		[
			forward 40
			right 30
		]
	]
]