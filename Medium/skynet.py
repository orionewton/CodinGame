import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Graphe:
    def __init__(self, n, *args):
        self.edges = [e for e in args]
        self.nodes = [i for i in range(n)]


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
node = []
exit = []
n, l, e = [int(i) for i in input().split()]
print(n, l, e, file=sys.stderr, flush=True)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 < n2:
        node.append((n1, n2))
    else:
        node.append((n2, n1))
node = Graphe(n, node)
node.edges[0].sort(key=lambda tup: (tup[0], tup[1]))
for i in range(e):
    exit.append(int(input()))  # the index of a gateway node

# game loop
while True:
    move = False
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    print(node.edges, file=sys.stderr, flush=True)

    for i in exit:
        print(si, i, file=sys.stderr, flush=True)
        if (si, i) in node.edges[0]:
            print(si, i)
            move = True
            node.edges[0].remove((si, i))
        elif (i, si) in node.edges[0]:
            print(i, si)
            move = True
            node.edges[0].remove((i, si))
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    if move is False:
        print(node.edges[0][0][0], node.edges[0][0][1])
        node.edges[0].pop(0)
