import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


def play(A, B):
    x = A[0]
    a = A[1]
    y = B[0]
    b = B[1]
    A[2] += str(y) + ' '
    B[2] += str(x) + ' '
    if a == b:
        if x < y:
            return 1
        return 0
    if a == 'C':
        if b == 'P' or b == 'L':
            return 1
        return 0
    if a == 'P':
        if b == 'R' or b == 'S':
            return 1
        return 0
    if a == 'R':
        if b == 'L' or b == 'C':
            return 1
        return 0
    if a == 'L':
        if b == 'S' or b == 'P':
            return 1
        return 0
    if b == 'C' or b == 'R':
        return 1
    return 0


n = int(input())
tab = []
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    tab.append([numplayer, signplayer, ''])
for i in tab:
    log(i)
while len(tab) > 1:
    log()
    for i in range(round(len(tab)/2)):
        tab.pop(i+play(tab[i], tab[i+1]))
    for j in tab:
        log(j)

print(tab[0][0])
print(tab[0][2][0:-1])
