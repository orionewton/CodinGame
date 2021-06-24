import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
result = 0
if n > 0:
    result = 5526
    for i in input().split():
        minus = False
    # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if t < 0:
            t = abs(t)
            minus = True
        if t == abs(result):
            if result < 0 and minus:
                result = t * -1
            else:
                result = t
        elif t < abs(result):
            if minus:
                result = t * -1
            else:
                result = t

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(result)
