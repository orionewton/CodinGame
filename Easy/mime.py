import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


def extan(s):
    i = -1
    ext = ''
    while i > -len(s):
        if s[i] == '.':
            ext = ext[::-1]
            return ext
        else:
            ext += s[i]
        i -= 1
    return ext[::-1]


n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext = {}
mt = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ex, m = input().split()
    ext[ex.lower()] = m
fname = []
for i in range(q):
    fname.append(input())  # One file name per line.

for i in fname:
    b = extan(i)
    if b in ext:
        print(ext[b])
    elif b.lower() in ext:
        print(ext[b.lower()])
    else:
        print("UNKNOWN")
# Write an answer using print


# For each of the Q filenames, display on a line the corresponding MIME type.
# If there is no corresponding type, then display UNKNOWN.
