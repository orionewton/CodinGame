import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


def values(c, lo, h, abc):
    c = c.upper()
    letter = []
    tmp = ''
    if ord(c) < 65 or ord(c) > 90:
        x = 26
    else:
        x = ord(c)-65
    for i in range(h):
        for j in range(lo):
            tmp += (abc[i][x*lo+j])
        letter.append(tmp)
        tmp = ''
    return letter


lo = int(input())
h = int(input())
t = input()
abc = []
for i in range(h):
    abc.append(input())

disp = ['' for i in range(h)]

for i in t:
    letter = values(i, lo, h, abc)
    for i in range(len(letter)):
        disp[i] += letter[i]

for i in disp:
    print(i)
