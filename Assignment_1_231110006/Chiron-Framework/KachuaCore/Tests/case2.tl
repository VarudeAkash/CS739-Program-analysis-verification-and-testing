:z = 55
:c = 92
pendown

if (:m >= 353) [
  if (:m + :x > 10001) [
    right 52
    left :m - 9500
    backward :m + :x - 365
  ]
] else [
  if (:m - :x - :y <= 57) [
    left :m
    right :m
    forward :m + :x + :y
    :x = :x - :y	
  ] 
]

if (:x + :z <= 512) [
  left :x
  forward :x
  :z = 21 + :x
] else [
  right :x + :z
  :z = 33 - :m
  backward 91
  :y = :y - :z
]

if (:y + :m <= 25) [
  repeat :z [
    forward :z
    :z = :z - 1
  ]
] else [
	backward 42
]

:z = :x + :y + :c
repeat :z [
  forward :z
  :z = :z - 1
]
