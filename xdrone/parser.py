from lark import Lark

xdrone_parser = Lark(r"""
fly: "fly" "(" ")" "{" takeoff command* land "}"

takeoff: "TAKEOFF" "(" ")"
land:    "LAND"    "(" ")"

?command: up
       | down
       | left
       | right
       | forward
       | backward
       | rotatel
       | rotater
       | wait

up: "UP" "(" distance ")"
down: "DOWN" "(" distance ")"
left: "LEFT" "(" distance ")"
right: "RIGHT" "(" distance ")"
forward: "FORWARD" "(" distance ")"
backward: "BACK" "(" distance ")"
rotatel: "ROTATELEFT" "(" angle ")"
rotater: "ROTATERIGHT" "(" angle ")"
wait: "WAIT" "(" seconds ")"

?number : INT
       | DECIMAL

?distance : number
?seconds  : number
?angle    : number

%import common.DECIMAL
%import common.INT

%import common.WS
%ignore WS

""", start='fly')