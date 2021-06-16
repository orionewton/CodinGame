import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lx, ly, x, y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    move = ''
    if ly > y:
        move += 'S'
        y = y+1
    elif ly < y:
        move += 'N'
        y = y-1
    if lx > x:
        move += 'E'
        x += 1
    elif lx < x:
        move += 'W'
        x -= 1

    print(move)
