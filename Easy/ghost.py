import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


w, h = [int(i) for i in input().split()]
tab = []

for i in range(h):
    line = input()
    if i == 0:
        starts = line.split()
    elif i == h-1:
        ends = line.split()
    else:
        tab.append(line)
for i in range(len(starts)):
    cursor = i*3
    for j in tab:
        if cursor == 0:
            if j[1] == '-':
                cursor += 3
        elif cursor == w-1:
            if j[cursor-1] == '-':
                cursor -= 3
        else:
            if j[cursor+1] == '-':
                cursor += 3
            elif j[cursor-1] == '-':
                cursor -= 3
    print(starts[i] + ends[int(cursor/3)])
