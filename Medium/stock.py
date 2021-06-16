import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
v = []
p = 0
tmp = 0
for i in input().split():
    v.append(int(i))
som = v[0]

for i in range(n):
    if v[i] > som:
        tmp = 0
        som = v[i]
    elif v[i] < som:
        tmp = v[i] - som
    if tmp < p:
        p = tmp
# Write an answer using print

print(p)
