import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


width, height = [int(i) for i in input().split()]
carte = [['#']*(width+2)]
for i in range(height):
    tmp = "#" + input() + '#'
    carte.append(list(tmp))
carte.append(['#']*(width+2))

for i in range(height+1):
    for j in range(width+1):
        if carte[i][j] != '#':
            if carte[i+1][j] != '#':
                carte[i][j] = str(int(carte[i][j])+1)
            if carte[i-1][j] != '#':
                carte[i][j] = str(int(carte[i][j])+1)
            if carte[i][j+1] != '#':
                carte[i][j] = str(int(carte[i][j])+1)
            if carte[i][j-1] != '#':
                carte[i][j] = str(int(carte[i][j])+1)
    if i > 0:
        prt = ''
        for k in carte[i]:
            prt += k
        print(prt[1:-1])
