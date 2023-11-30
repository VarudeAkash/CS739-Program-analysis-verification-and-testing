if(:x > 150)[
	if(:x==:y)[
		right :x/2
		forward :y/3
	]
	left -:x/2
	forward :y
	if(:x > :y)[
		penup
		right :y/2
		forward :x/2
		if(:y<0)[
			if(:y<-100)[
				left 30
				forward :y/4
			]
			else[
				left 45
				forward :y
			]
		]
		else[
			if(:y<100)[
				right 45
				pendown
				forward :y
			]
			else[
				if(:x<400)[
					right :x/4
					forward :x/2
				]
				else[
					if(:y<300)[
						penup
						left 30
						forward :y/2
					]
					else[
						right :y/6
						forward :y/4
					]
					penup
				]
			forward :y/3
			]
		]
	]
	else[
		penup
		left 30
		forward :y
		if(:y<0)[
			left 30
		]
		else[
			pendown
			right :y/2
			forward :x
		]
		forward :y/3
	]
	]
else[
	if(:x<0)[
		right :x/2
		forward :y/2
		penup
		if(:x > :y)[
			
			if(:y<-300)[
				pendown
				left :x/2
				forward :y/5
			]
			else[
				if(:x>-100)[
					right :x/2
					forward :y/2
				]
				else[
					pendown
					left :y/3
					forward :y/3
				]
				forward :x/4
			]
		]
		else[
			if(:y==500)[
				pendown
				goto(0,0)
			]
			else[
				if(:y<0)[
					pendown
					forward :y/2
				]
				else[
					right :y/3
					forward :x/4
				]
				forward :x/5
			]			
		]
		forward :x/3
	]
	else[
		if(:y>0)[
			forward :x - 100
			if(:x<:y)[
				right :x/4
				forward -:x/3
				penup
			]
			else[
				left :x/3
				forward :x/3
			]
			if(:x<100)[
				right 30
				forward :x/2
			]
			else[
				penup
				left :x/3
				:x = :x -45
				forward :y/2
			]
		]
		else[
			left -:y/3
			forward :y/3
			if(:x<100)[
				right :y/3
				forward :y/2
			]
			else[
				left 30
				forward :y/3
				penup
			]
			forward :x/3
		]
	]
]
