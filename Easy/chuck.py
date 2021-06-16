import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
byte = ''
for x in bytearray(message, 'utf-8'):
    ch = str(''.join(format(x, 'b') ))
    while len(ch) <7:
        ch = '0' + ch
    byte= byte + ch

ans = ''
state = False
for i in byte+'2':
    if state is True:
        if i == prev:
            cpt +=1
        else:
            state = False
            for j in range(cpt):
                ans = ans + '0'
            ans = ans + ' '
    if state is False:
        if i == '1':
            ans = ans + '0 '
            prev = '1'
        elif i == '0':
            ans = ans + '00 '
            prev = '0'
        state = True
        cpt = 1
ans = ans[:-1]

print(ans)
