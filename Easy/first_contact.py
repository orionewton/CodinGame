import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


def encode(message):
    rep = ''
    ln = len(message)
    i = 1
    while len(rep) < ln:
        tmp = message[:i]
        message = message[i:]
        if i % 2 == 0:
            rep = tmp + rep
        else:
            rep = rep + tmp
        i += 1
    return rep


def indi(message, tab):
    i = 1
    while sum(tab) < len(message):
        tab.append(i)
        i += 1
    while sum(tab) > len(message):
        tab[-1] -= 1
    return tab


def decode(message, tab):
    rep = ''
    first = False
    if (tab[1] % 2 == 0 and tab[0] % 2 == 0) or (tab[1] % 2 != 0 and tab[0] % 2 != 0):
        first = True
    if first:
        if tab[0] % 2 == 0:
            tmp = message[-tab[0]:]
            message = message[:-tab[0]]
            rep = tmp + rep
        else:
            tmp = message[:tab[0]]
            message = message[tab[0]:]
            rep = tmp + rep
    tab.pop(0)
    for i in tab:
        if i % 2 == 0:
            tmp = message[:i]
            message = message[i:]
            rep = tmp + rep
        else:
            tmp = message[-i:]
            message = message[:-i]
            rep = tmp + rep
    return rep


n = int(input())
code = False
if n < 0:
    code = True
message = input()
log(message)
ln = len(message)
for j in range(abs(n)):
    if code:
        message = encode(message)
    else:
        tab = indi(message, [])
        tab.reverse()
        message = decode(message, tab)

print(message)
