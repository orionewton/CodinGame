import sys
import math

# Don't let the machines win. You are humanity's last hope...

maxx = int(input())  # the number of cells on the X axis
maxy = int(input())  # the number of cells on the Y axis

node = []
nodes = 0

for i in range(maxy):
    line = input()  # width characters, each either 0 or .
    l = []
    for j in line:
        if j == "0":
            l.append(1)
            nodes += 1
        else:
            l.append(0)
    node.append(l)

for i in range(nodes):
    for y in range(maxy):
        for x in range(maxx):
            out = ""
            if node[y][x] == 1:
                out += str(x) + " " + str(y) + " "
                if x == maxx-1:
                    out += "-1 -1 "
                else:
                    neighboor = False
                    for x1 in range(x+1, maxx):
                        if node[y][x1] == 1:
                            out += str(x1) + " " + str(y) + " "
                            neighboor = True
                            break
                    if neighboor is False:
                        out += "-1 -1 "
                if y == maxy-1:
                    out += "-1 -1 "
                else:
                    neighboor = False
                    for y1 in range(y+1, maxy):
                        if node[y1][x] == 1:
                            out += str(x) + " " + str(y1) + " "
                            neighboor = True
                            break
                    if neighboor is False:
                        out += "-1 -1 "
                node[y][x] = 0           
# Three coordinates: a node, its right neighbor, its bottom neighbor
                print(out)
