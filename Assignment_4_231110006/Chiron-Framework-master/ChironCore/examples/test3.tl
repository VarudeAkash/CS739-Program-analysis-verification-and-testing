:a = 50
:b = 20 
if :a <= 100[
	if :a<= 40[
		forward 50
	]
	else[
		if :b <= 30[
			
			forward 20
			left 90
			forward 50
		]
		else[
			backward 100
		]
	]
	
]
else[
	right 50
]