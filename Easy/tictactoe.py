import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


win = False
tab = []
for i in range(3):
    tab.append(input())
for i in tab:
    log(i)
diag = tab[0][0] + tab[1][1] + tab[2][2]
diag2 = tab[0][2] + tab[1][1] + tab[2][0]
for i in range(len(tab)):
    if tab[i].count("O") == 2 and tab[i].count(".") == 1:
        tab[i] = "OOO"
        win = True
        break
    col = []
    tmp = ''
    for j in range(len(tab)):
        tmp += tab[j][i]
    col.append(tmp)
    log(col)
    if col[0].count("O") == 2 and col[0].count(".") == 1:
        n = col[0].index(".")
        tmp = ''
        for j in range(len(tab[n])):
            if tab[n][j] == "." and j == i:
                tmp += "O"
                win = True
            else:
                tmp += tab[n][j]
        tab[n] = tmp
        break
    if diag.count("O") == 2 and diag.count(".") == 1:
        n = diag.index(".")
        tmp = ''
        for j in range(len(tab[n])):
            if tab[n][j] == "." and j == n:
                tmp += "O"
                win = True
            else:
                tmp += tab[n][j]
        tab[n] = tmp
        break
    if diag2.count("O") == 2 and diag2.count(".") == 1:
        n = diag2.index(".")
        tmp = ''
        for j in range(len(tab[n])):
            if tab[n][j] == "." and j == n:
                tmp += "O"
                win = True
            else:
                tmp += tab[n][j]
        tab[n] = tmp
        break

if win:
    for i in tab:
        print(i)
else:
    print("false")
