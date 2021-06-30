import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


def caesar(s, i, code):
    caesar = ''
    cpt = 0
    for c in s:
        if code:
            mod = ord(c) + i + cpt
            while mod > 90:
                mod -= 26
        else:
            mod = ord(c) - i - cpt
            while mod < 65:
                mod += 26
        caesar += chr(mod)
        cpt += 1
    return caesar


operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotors.append(input())
message = input()
if operation == 'ENCODE':
    code = True
else:
    code = False
log(message)
tmp = ''
if code:
    message = caesar(message, pseudo_random_number, code)
    for i in message:
        c = i
        for j in rotors:
            c = j[ord(c) % 64 - 1]
        tmp += c
else:
    rotors.reverse()
    for i in message:
        c = i
        for j in rotors:
            c = chr(j.index(c)+65)
        tmp += c
    tmp = caesar(tmp, pseudo_random_number, code)
# Write an answer using print
print(tmp)
