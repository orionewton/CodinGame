import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
cpt=0
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # _dist: distance to the next checkpoint
    # angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, dist, angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"

    thrust = 0

    if dist < 300:
        thrust = 0
    else:
        thrust = 100

    if abs(angle) > 90:
        thrust = 0

    if dist > 8000 and abs(angle) < 10 and cpt == 0:
        thrust = "BOOST"
        cpt = 1

    move = str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust)

    print(move)
