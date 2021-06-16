import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def log(x):
    print(x, file=sys.stderr, flush=True)


def play(n, x, y, pos):
    std = [1, 3, 7, 8, 9, 12, 13]
    if n in std:
        print(x, y+1)
        return
    if n == 2 or n == 6:
        if pos == 'LEFT':
            print(x+1, y)
            return
        print(x-1, y)
        return
    if n == 4 or n == 10:
        if pos == 'TOP':
            print(x-1, y)
            return
        print(x, y+1)
        return
    if n == 5 or n == 11:
        if pos == 'TOP':
            print(x+1, y)
            return
        print(x, y+1)
        return


# w: number of columns.
# h: number of rows.
mape = []
tmp = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    line = line.split()
    tmp = map(int, line)
    mape.append(list(tmp))
    # represents a line in the grid and contains W integers.
    # Each integer represents one room of a given type.
for i in mape:
    log(i)
ex = int(input())
# the coordinate along the X axis of the exit

# game loop
while True:
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    pos = inputs[2]
    log(pos)
    log(mape[y][x])
    # log(mape[x][y])
    play(mape[y][x], x, y, pos)

    # Write an action using print

    # One line containing the X Y coordinates of the room in which you believe
    # Indy will be on the next turn.
