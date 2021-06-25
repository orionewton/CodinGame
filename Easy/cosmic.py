import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


planet = []
n = int(input())
for i in range(n):
    name, *rmc = input().split()
    r, m, c = (float(s) for s in rmc)
    dP = m / (4/3 * math.pi * pow(r, 3))
    if name == 'Alice':
        rA = r
        dA = dP
        # log([name, r, m, c, dP])
    else:
        planet.append([name, r, m, c, dP])
# log(planet)

mini = sys.maxsize
for i in planet:
    rl = rA * (2 * dA/i[4])**(1./3.)
    # log(i[0])
    # log(rl)
    # log(i[3])
    if i[3] > rl and i[3] < mini:
        mini = i[3]
        name = i[0]
        # log([name, mini])
    # log("")
print(name)
