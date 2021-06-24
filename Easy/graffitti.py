import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


l = int(input())
n = int(input())
paint = ''
wall = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    wall.append((st, ed))
wall.sort(key=lambda tup: (tup[0], tup[1]))
ind = 0
log(wall)
pr = True
while len(wall) > 0:
    if ind < wall[0][0]:
        print(ind, wall[0][0])
        pr = False
        ind = wall[0][1]
        wall.pop(0)
    else:
        ind = max(ind, wall[0][1])
        wall.pop(0)
if ind == l and pr:
    print("All painted")
elif ind != l:
    print(ind, l)
