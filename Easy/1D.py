import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def log(x):
    print(x, file=sys.stderr, flush=True)


def calc(op, wait, k):
    i = wait[k]
    operation = i[0]
    arg_1 = i[1]
    arg_2 = i[2]
    if '$' in arg_1:
        ind = int(arg_1[1:])
        if op[ind] is not False:
            arg_1 = op[ind]
        else:
            calc(op, wait, ind)
            arg_1 = op[ind]
    log(arg_1)
    if '$' in arg_2:
        ind = int(arg_2[1:])
        if op[ind] is not False:
            arg_2 = op[ind]
        else:
            calc(op, wait, ind)
            arg_2 = op[ind]

    if operation == "VALUE":
        op[k] = int(arg_1)
    elif operation == "ADD":
        op[k] = (int(arg_1)+int(arg_2))
    elif operation == "SUB":
        op[k] = (int(arg_1)-int(arg_2))
    elif operation == "MULT":
        op[k] = (int(arg_1)*int(arg_2))
    wait.pop(k)


n = int(input())
op = []
wait = {}
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    if operation == "VALUE":
        if '$' not in arg_1:
            op.append(int(arg_1))
        else:
            ind = int(arg_1[1:])
            if ind < i and op[ind] is not False:
                op.append(op[ind])
            else:
                op.append(False)
                wait[i] = [operation, arg_1, arg_2]
    else:
        if('$' not in arg_1 and '$' not in arg_2):
            if operation == "ADD":
                op.append(int(arg_1)+int(arg_2))
            elif operation == "SUB":
                op.append(int(arg_1)-int(arg_2))
            elif operation == "MULT":
                op.append(int(arg_1)*int(arg_2))
        else:
            doable = True
            if '$' in arg_1:
                ind = int(arg_1[1:])
                if ind < i and op[ind] is not False:
                    arg_1 = str(op[ind])
                else:
                    doable = False

            if '$' in arg_2 and doable:
                ind = int(arg_2[1:])
                if ind < i and op[ind] is not False:
                    arg_2 = str(op[ind])
                else:
                    doable = False
            if doable:
                if operation == "ADD":
                    op.append(int(arg_1)+int(arg_2))
                elif operation == "SUB":
                    op.append(int(arg_1)-int(arg_2))
                elif operation == "MULT":
                    op.append(int(arg_1)*int(arg_2))
            else:
                op.append(False)
                wait[i] = [operation, arg_1, arg_2]

while len(wait) > 0:
    res = list(wait.keys())[0]
    calc(op, wait, res)

for i in op:
    # Write an answer using print
    print(i)
