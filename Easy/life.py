import sys
import math
from copy import deepcopy


def log(x):
    print(x, file=sys.stderr, flush=True)


def voisins(tab, i, j):
    tot = 0
    if tab[i+1][j+1] == 'O':
        tot += 1
    if tab[i+1][j] == 'O':
        tot += 1
    if tab[i+1][j-1] == 'O':
        tot += 1

    if tab[i][j+1] == 'O':
        tot += 1
    if tab[i][j-1] == 'O':
        tot += 1

    if tab[i-1][j+1] == 'O':
        tot += 1
    if tab[i-1][j] == 'O':
        tot += 1
    if tab[i-1][j-1] == 'O':
        tot += 1
    return tot


def res(cond, tot):
    if cond[tot] == '1':
        return True
    return False


def death(cond, tot):
    if cond[tot] == '0':
        return True
    return False


ymax, xmax, n = [int(i) for i in input().split()]
alive = input()
dead = input()
carte = ['.'*(xmax+2)]
for i in range(ymax):
    line = '.' + input() + '.'
    carte.append(line)
carte.append('.'*(xmax+2))
for i in range(len(carte)-1):
    if i > 0:
        prt = ''
        for j in range(xmax+2):
            prt += carte[i][j]
        log(prt[1:-1])
log('')

for k in range(n):
    grid = [['.']*(xmax+2) for j in range(ymax+2)]
    for i in range(ymax+1):
        if i > 0:
            tot = 0
            for j in range(xmax+1):
                if j > 0:
                    grid[i][j] = carte[i][j]
                    tot = voisins(carte, i, j)
                    if grid[i][j] == '.' and res(dead, tot):
                        grid[i][j] = 'O'
                    elif grid[i][j] == 'O' and death(alive, tot):
                        grid[i][j] = '.'
    carte = deepcopy(grid)
# Write an answer using print
for i in range(len(carte)-1):
    if i > 0:
        prt = ''
        for j in range(xmax+2):
            prt += carte[i][j]
        print(prt[1:-1])
