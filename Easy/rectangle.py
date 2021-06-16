import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



w, h, count_x, count_y = [int(i) for i in input().split()]
coupeX = [0]
coupeY = [0]
tot = 0
for i in input().split():
    x = int(i)
    coupeX.append(x)
for i in input().split():
    y = int(i)
    coupeY.append(y)

coupeX.append(w)
coupeY.append(h)

# Write an answer using print
print(coupeX, coupeY, file=sys.stderr, flush=True)

subx = []
tmp = []
suby = []

for i in coupeX:
    for j in coupeX:
        if i > 0:
            if i > j:
                tmp.append([i - j, 1])

tmp.sort()

n = 0
for i in range(len(tmp)):
    if n == 0:
        subx.append(tmp[i])
        n += 1
    elif tmp[i][0] == tmp[i-1][0]:
        subx[n-1][1] += 1
    else:
        subx.append(tmp[i])
        n += 1

tmp = []
for i in coupeY:
    for j in coupeY:
        if i > 0:
            if i > j:
                tmp.append([i - j, 1])

tmp.sort()

n = 0
for i in range(len(tmp)):
    if n == 0:
        suby.append(tmp[i])
        n += 1
    elif tmp[i][0] == tmp[i-1][0]:
        suby[n-1][1] += 1
    else:
        suby.append(tmp[i])
        n += 1

i = 0
j = 0
while i < len(subx) and j < len(suby):
    if subx[i][0] == suby[j][0]:
        tot += subx[i][1] * suby[j][1]
        i += 1
        j += 1
    elif subx[i][0] < suby[j][0]:
        i += 1
    else:
        j += 1

print(str(tot))
