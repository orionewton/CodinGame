import sys
import math


def nextk(k):
    s = 0
    for i in str(k):
        s += int(i)
    return k+s


r_1 = int(input())
r_2 = int(input())

while r_1 != r_2:
    if r_1 < r_2:
        r_1 = nextk(r_1)
    else:
        r_2 = nextk(r_2)

print(r_1)
