import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


n = int(input())
start = []
for i in range(n):
    j, d = [int(j) for j in input().split()]
    start.append((j, j+d-1))

start.sort(key=lambda tup: (tup[1], tup[0]))
# Write an answer using print
sol = [start[0]]
for i in range(len(start)):
    if start[i][0] > sol[-1][1]:
        sol.append(start[i])

print(len(sol))
