import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
mini = 1000
maxi = 2
for i in input().split():
    a = (int(i))
    if a < mini:
        mini = a
    elif a > maxi:
        maxi = a

tot = max(maxi, l-mini)
# Write an answer using print

print(tot)
