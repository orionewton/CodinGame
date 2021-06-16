import sys
import math


def convert(i):
    if i[1] == '0':
        return 10
    elif i[0] == 'J':
        return 11
    elif i[0] == 'Q':
        return 12
    elif i[0] == 'K':
        return 13
    elif i[0] == 'A':
        return 14
    else:
        return int(i[0])


def compare(i, j):
    if i < j:
        return 2
    elif i > j:
        return 1
    return 0


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
game = True
bat = False
nb = 0
p1 = []
p2 = []
tmp1 = []
tmp2 = []
tmp = []
n = int(input())  # the number of cards for player 1
for i in range(n):
    p1.append(convert(input()))  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    p2.append(convert(input()))  # the m cards of player 2

# Write an answer using print

while game:
    if len(p1) == 0 and len(p2) > 0:
        print("2", nb)
        break
    if len(p2) == 0 and len(p1) > 0:
        print("1", nb)
        break
    if len(p1) == 0 and len(p2) == 0:
        print("PAT")
        break
    print("P1", p1, file=sys.stderr, flush=True)
    print("P2", p2, file=sys.stderr, flush=True)
    print(" ", nb, file=sys.stderr, flush=True)
    m = compare(p1[0], p2[0])
    if m == 1:
        tmp.append(p1[0])
        tmp.append(p2[0])
        if bat:
            tmp1.append(p1[0])
            tmp2.append(p2[0])
            for i in tmp1:
                p1.append(i)
            for i in tmp2:
                p1.append(i)
            tmp = []
            tmp1 = []
            tmp2 = []
            bat = False
        p1.pop(0)
        p2.pop(0)
        for i in tmp:
            p1.append(i)
        tmp = []
        nb += 1
    elif m == 2:
        tmp.append(p1[0])
        tmp.append(p2[0])
        if bat:
            tmp1.append(p1[0])
            tmp2.append(p2[0])
            for i in tmp1:
                p2.append(i)
            for i in tmp2:
                p2.append(i)
            tmp = []
            tmp1 = []
            tmp2 = []
            bat = False
        p1.pop(0)
        p2.pop(0)
        for i in tmp:
            p2.append(i)
        tmp = []
        nb += 1
    else:
        if len(p1) < 4 and len(p2) >= 4:
            print("PAT")
            break
        if len(p2) < 4 and len(p1) >= 4:
            print("PAT")
            break
        if len(p2) < 4 and len(p1) < 4:
            print("PAT")
            break
        bat = True
        tmp1.append(p1[0])
        p1.pop(0)
        tmp1.append(p1[0])
        p1.pop(0)
        tmp1.append(p1[0])
        p1.pop(0)
        tmp1.append(p1[0])
        p1.pop(0)
        tmp2.append(p2[0])
        p2.pop(0)
        tmp2.append(p2[0])
        p2.pop(0)
        tmp2.append(p2[0])
        p2.pop(0)
        tmp2.append(p2[0])
        p2.pop(0)
