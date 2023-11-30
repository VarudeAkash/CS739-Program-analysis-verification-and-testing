if (:x > :y) [
    penup
    if (:x > 300) [
        right (:y / 2)
        forward :y/3
        if (:y > 100) [
            left 90
            pendown
        ] else [
            right 90
            forward :x/4
            pendown
        ]
        forward :x/3
    ] else [
		pendown
        left (:y / 2)
        forward :x
		
        if (:y < 50) [
            left (:x / 3)
            penup
            if (:x < 0) [
                right 45
				pendown
                forward :x/3
            ] else [
                left 60
            ]
			pendown
            forward (:y / 2)
        ] else [
            right (:x - 100)
            forward :y/2
            if (:x < 100) [
                penup
                left :x/2
            ] else [
                right 30
                forward :y/3
            ]
            forward (:x - :y)
        ]
    ]
]
else[
	:temp = :x
	:x = :y
	:y = :x
	left (:x-:y)
    forward :x/3
    penup
    if (:x > 200) [
        right (:y / 2)
        forward :y/3
		pendown
        if (:y > 0) [
            left 90
        ] else [
            right :x/4
            forward :x/2
            penup
        ]
        forward :x/2
    ] else [
        left (:y / 2)
        forward :x/3
        if (:y < 0) [
            left (:x / 3)
            pendown
            if (:x < 0) [
                right 45
                forward :x/3
            ] else [
                left :y/3
            ]
            forward (:y / 2)
        ] else [
            pendown
            right (:x - 100)
            forward :y
            if (:x < 50) [
                penup
                left :x/4
            ] else [
                right :y/2
                forward :y/3
            ]
            forward (:x - :y)
        ]
    ]

]
