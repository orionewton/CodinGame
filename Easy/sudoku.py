import sys
import math
import itertools
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


tab = [[0 for i in range(9)] for i in range(9)]
cols = [[0 for i in range(9)] for i in range(9)]
sub = []


def getQuadrant(tab, ind):
    sub = []

    row = (ind // 3) * 3
    col = (ind % 3) * 3

    for i in range(3):
        for j in range(3):
            sub.append(tab[row + i][col + j])

    return sub


for i in range(9):
    k = 0
    for j in input().split():
        tab[i][k] = int(j)
        k += 1

for i in tab:
    log(i)

val = 'true'
for i in range(9):
    if len(set(tab[i])) < 9 or sum(tab[i]) != 45:
        val = 'false'
    for j in range(9):
        cols[i][j] = tab[j][i]
    sub.append(getQuadrant(tab, i))

for i in range(9):
    if len(set(cols[i])) < 9 or sum(cols[i]) != 45:
        val = 'false'
    if len(set(sub[i])) < 9 or sum(sub[i]) != 45:
        val = 'false'


# Write an answer using print

print(val)
