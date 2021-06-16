import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


n = int(input())
coo = []
xi = []
yi = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    coo.append((x, y))
    xi.append(x)
    yi.append(y)
coo.sort(key=lambda tup: tup[1])
m = coo[int(n/2)][1]
tot = max(xi) - min(xi)
for i in coo:
    tot += abs(i[1] - m)

# Write an answer using print

print(tot)
