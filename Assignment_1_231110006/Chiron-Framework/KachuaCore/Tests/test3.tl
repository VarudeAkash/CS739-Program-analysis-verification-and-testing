if (:x > :y) [
    if (:x > 300) [
        right :y/2
        forward :y
        if (:y > 100) [left 90
		pendown] else [right 90
		forward :x/2
		]
        forward :y/3
    ] else [
        penup
        left :y/2
        forward :x/3
        if (:y < 0) [
            left :x/3
			pendown
            if (:x < 200)[right :x/5
				forward :x/3
			] else[
			left 60
			]
            forward :y/2
        ] else [
            pendown
            right :x-100
            forward :y
            if (:x < 100)[
				left :x
			] else[
				right 30
				forward :y
			]
            forward :x-:y
        ]
    ]
] 
else [
    if (:x < 0) [
        right :y/6
        forward :x/5

        if (:x > -200) [
			penup
            left :y/2
            forward :y/3
            if (:y > 0) [
				:y=-:y
				right 90
				forward :y/3
			] else[
				left :y/2
				
			]
			goto(:x,0)
            forward :y
        ] else [
            right :x/3
            goto(0, :y)
			pendown
            forward :y/5
            if (:y > 0)[
				left :y
				goto(0,0)
				forward :x/2
			] else [right :x/6]
            forward :x/3
        ]
    ] else [
        if (:y > 250) [
			pendown
            forward (:x - 100)
            if (:x < 100) [
				penup
                right :x/2
                forward -:x/2
                if (:y > 300)[
					left :x
					pendown
				] else [right :y/5]
                forward -:x
            ] 
			else [
                left :y/2
                forward :x
                if (:x < 400) [right 30] else [left 60]
                forward :y-:x
            ]
            if (:x < 100) [right 30]
			else[
				penup
				left :x/2
				forward :x-:y]
            if (:y < 400) [right -:x
				pendown
				forward :y
				
			] else [left -:x/2]
            forward :x/3
        ] else [
			pendown
            left :y/2
            forward :x/3
            if (:x < 100) [forward :x
			penup] else [left :x/3]
            forward :y
            if (:y > 150) [forward :y/2]
			else[
				penup
				right :x/3
			]
			forward :x
        ]
    ]
]
