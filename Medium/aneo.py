import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


def rouge(s, d, t):
    if (18 * d) % (10 * s * t) >= (5 * s * t):
        return True
    return False


speed = int(input())
light_count = int(input())
d = []
t = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    d.append(distance)
    t.append(duration)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

s = speed
li = light_count

i = 0
while i < li:
    if (rouge(s, d[i], t[i])):
        s -= 1
        i = -1
    i += 1

print(s)
