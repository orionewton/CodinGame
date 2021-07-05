import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


def points(n):
    tmp = n
    if tmp > 4:
        i = 0
        while tmp >= 2:
            i += 1
            tmp = tmp / 2
        return (2**i)*(i-1)
    else:
        return 4


tab = []
som = 0
tmp = 0
for i in range(4):
    for j in input().split():
        cnt = int(j)
        tab.append(cnt)
fours = int(input())
for i in range(4):
    log(tab[4*i:4*i+4])
for i in tab:
    tmp += i
    if i > 2:
        som += points(i)
if fours < 0:
    fours = 0
tot = som - fours*4
print(tot)
print(round(tmp/2)-fours-2)
