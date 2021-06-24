import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


def move(active, t):
    tmp = min(active)
    r = len(active)
    if r > len(t):
        r = len(t)
    for i in range(r):
        t[i] -= tmp
        if t[i] <= 0:
            ind = i
    t.pop(ind)
    return tmp


r = int(input())
v = int(input())
t = []
timer = 0
for i in range(v):
    c, n = [int(j) for j in input().split()]
    t.append(pow(5, c-n)*pow(10, n))

active = t[:r]
while len(t) > 0:
    if len(t) <= r:
        timer += max(t)
        break
    else:
        timer += move(active, t)
        active = t[:r]
print(timer)
