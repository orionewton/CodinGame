import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


n = int(input())
log(n)
minus = False
if n < 0:
    n = -n
    minus = True

tern = ""

while(n > 0):
    res = n % 3
    n = n // 3
    if(res == 2):
        res = -1
        n += 1

    if(res == 0):
        tern = '0' + tern
    else:
        if(res == 1):
            if minus:
                tern = 'T' + tern
            else:
                tern = '1' + tern
        else:
            if minus:
                tern = '1' + tern
            else:
                tern = 'T' + tern

if tern == "":
    tern = "0"

print(tern)
