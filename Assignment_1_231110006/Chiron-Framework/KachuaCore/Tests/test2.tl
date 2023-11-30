if(:x>0)[
	if(:y>0)[
		if(:x==:y)[
			if(:x<100)[
				left 45
				forward :x
			]
			else[
				if(:x<300)[
					right :x/2
					penup
					forward :x/3
				]
				else[
					if(:x<400)[
						left 30
						forward :x/4
					]
					else[
						if(:x==500)[
							right 50
							forward 30
						]
						else[
							right 35
							forward :x/5
						]
					]
				]
			]
		]
		else[
			left :x/2
			if(:x<100)[
				if(:x>:y)[
					forward :x
				]
				else[
					left 30
					forward :y/3
				]
			]
			else[
				right :x/2
				if(:x<300)[			
					if(:x>:y)[
						forward :x/2
						right 45
					]
					else[
						forward :y/2
						left 60
					]
					forward :x/2
					goto(:x,:y)
				]
				else[
					left 30
					goto(0,100)
					if(:x<400)[				
						if(:x>:y)[
							left 50
							forward :x/4
						]
						else[
							left 60
							forward :y/5
						]
						goto(:x,:y)
					]
					else[
						if(:x==500)[				
							forward :x/5
						]
						else[
							left :y/3
						]
						penup
					]
					pendown
					forward :y/2
				]
			]
		]
	]
	else[
		right :y/3
		if(:y<-200)[
			goto(0,-100)
			left :y/2
			forward :y/2
		]
		else[
			forward :x/3
			penup
			if(:x>100)[
				pendown
				if(:y==-500)[
					forward :x/5
				]
				else[
					right 45
					forward :y/3
				]
				forward 30
			]
			else[
				goto(0,0)
				if(:y<500)[
					pendown
					if(:y<200)[
						forward :y/3
						left :y/3
					]
					else[
						forward :x/3
						penup
					]
					right :x/4
				]
				else[
					forward :x/3
					right :x/2
				]
				forward :y/2
			]
			left :x/2
		]
		forward :y/3
	]
]
else[
	right :y/2
	if(:y>0)[
		forward :x/2
		if(:x<-100)[
			penup
			if(:y>100)[
				if(:y>300)[
					forward :y/2
					left :x/3
				]
				else[
					left :y/2
					pendown
				]
				forward 30
			]
			else[
				pendown
				right 45
				forward :y/3
			]
			goto(:x/2,:y/2)
		]
		else[
			goto(200,:x/2)
		]
		left :x/2
		forward :y/2
		
	]
	else[
		penup
		if(:x==:y)[
			forward :x/2
		]
		else[
			forward :x/5
			right :x/2
			if(:x>-500)[
				if(:x>-400)[
					pendown
					if(:x>-100)[
						forward :x/3
						left :y/2
					]
					else[
						right :x/3
						penup
					]
					goto(:x,:y)
				]
				else[
					forward :x/2
					if(:y<-300)[
						pendown
						goto(:y,0)
						forward :y
					]
					else[
						pendown
						forward :x/3
					]
					pendown
					goto(:y,:x)
				]
			]
			else[
				forward :x/5
			]
			forward :x/3
		]
		left :x/3
		forward :y/2
	]
]