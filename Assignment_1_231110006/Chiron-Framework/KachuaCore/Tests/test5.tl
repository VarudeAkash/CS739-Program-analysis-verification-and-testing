if(:x >0)[
	left :y
	if(:x>:y)[
		pendown
		if(:x>2*:y)[
			right :y
			penup
		]
		else[
			if(:x > -:y)[
				left :x
				forward -:y
			]
			forward :x/3
			left :y/2
			right :x
		]
		forward :y
		left :x
		pendown 
		forward (:y)
		
	]
	else[
		pendown
		forward (:x - :y)
		left :y
		forward :y
		goto(:x,0)
		if(:y < 200)[
			forward :y/2
			penup
			left :x/3
			forward :y
		]
		else[
			right :y/2
			if(:y>:x*3)[
				forward :x
				left (:y-:x)
			]
			else[
				penup
				right :x/2
			]
			forward :y
		]
	]
]
else[
	if(:x<:y)[
		if(:y>0)[
			penup
			forward :y
			left :x
			pendown 
			forward :x*2
			right (:x + :y)
			forward (:x -:y)
		]
		else[
			pendown
			left :y
		]
		pendown
		forward -:x*2
	]
	else[
		left :x
		if(-:x > -:y)[
			forward :x
			penup
		]
		else[
			if(-:x > :y)[
				left :y/2
				forward -:x/2
			]
			pendown
			goto(0,:y)
			right :y
			if(-2*:x > :y)[
				right :x
				penup
				forward :y/2
			]
			forward :x*2
			left :y
		]
		forward :y
	]

]