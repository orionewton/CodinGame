import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
tmp = []
for i in input().split():
    tmp.append(int(i))

mini = min(tmp)
maxi = max(tmp)
tot = max(maxi, l-mini)
# Write an answer using print

print(tot)
