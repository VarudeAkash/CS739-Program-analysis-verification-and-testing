:m = 90
:c = 100
pendown
if (:m + :c >= :x + :y) [
	if (:x <= 512) [
		repeat 2 [
			forward :m + :x
			backward :m + :x	
		]
	] else [
		repeat 2 [
			forward :m + :y	
		]
	]
]

if (:c >= :y) [
	if (:y >= 512) [
		repeat 2 [
			forward 5
			backward :m + :x	
		]
	] else [
		repeat 2 [
			backward :m + 1000	
		]
	]
]
