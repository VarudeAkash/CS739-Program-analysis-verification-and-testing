penup
if :x > :y [
	if :y > :z [
		if :x > 0 [
			right 100
			backward 200
		]
		else [
			if :y > 0[
				left 50
				forward 200
			]
			else[
				forward 200
			]
		]
	]
	else[
		if :y > 0[
			left 50
			forward 200
		]
		else[
			if :z > 0[
				left 150
				forward 400
			]
			else[
				backward 300
			]
		]
	]
]
else[
	if :y > 0[
		left 50
		forward 200
	]
	else[
		if :z > 0[
			left 150
			forward 400
		]
		else[
			backward 300
		]
	]
]
