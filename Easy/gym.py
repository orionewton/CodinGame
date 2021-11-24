import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


gymnasts = input().split(',')
categories = input().split(',')
n = int(input())
scores = []
for i in range(n):
    row = input()
    scores.append(row.split(','))

log(gymnasts)
log(categories)
for i in scores:
    log(i)

for i in range(len(gymnasts)):
    gym = gymnasts[i]
    ret = []
    for k in categories:
        if k == "bars":
            k = 1
        elif k == "beam":
            k = 2
        else:
            k = 3
        maxi = 0
        for j in scores:
            if (j[0] == gym) and (float(j[k]) > maxi):
                maxi = float(j[k])
        if maxi % 1 == 0:
            maxi = int(maxi)
        ret.append(str(maxi))
    print(','.join(ret))
