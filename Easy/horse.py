import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mini = 10000000
pi = []
p = 0
n = int(input())
for i in range(n):
    pi.append(int(input()))
    p += 1

pi.sort()

for i in range(p):
    if i > 0:
        mini = min(mini, pi[i]-pi[i-1])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(mini)
