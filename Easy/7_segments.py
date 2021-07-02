import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


tab = []
line_1 = input()
tab.append(line_1)
line_2 = input()
tab.append(line_2)
line_3 = input()
tab.append(line_3)

rep = ''
for i in range(round(len(line_1)/3)):
    num1 = line_1[i*3:i*3+3]
    num2 = line_2[i*3:i*3+3]
    num3 = line_3[i*3:i*3+3]
    if num1[1] == ' ':
        # 1 or 4
        if num2[1] == '_':
            nb = '4'
        else:
            nb = '1'
    elif num2[0] == ' ':
        # 2, 3 or 7
        if num2[1] == ' ':
            nb = '7'
        elif num3[0] == ' ':
            nb = '3'
        else:
            nb = '2'
    elif num3[0] == ' ':
        # 5 or 9
        if num2[2] == ' ':
            nb = '5'
        else:
            nb = '9'
    elif num2[1] == ' ':
        nb = '0'
    elif num2[2] == ' ':
        nb = '6'
    else:
        nb = '8'
    rep += nb

print(rep)
