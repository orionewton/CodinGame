import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


def nextk(k):
    s = 0
    for i in str(k):
        s += int(i)
    return k+s


ret = "NO"
r_1 = int(input())
r_2 = r_1-(len(str(r_1))*10)

if r_2 <= 0:
    r_2 = 1

log(r_1, r_2)

while r_2 < r_1 and ret == "NO":
    riv = r_2
    log("river", riv)
    while riv <= r_1:
        if riv == r_1:
            ret = "YES"
            break
        riv = nextk(riv)
        log(riv)
    r_2 += 1

print(ret)
