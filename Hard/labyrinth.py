import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def voinsins(self):
        res = []
        res.append(Coords(self.x, self.y-1))
        res.append(Coords(self.x+1, self.y))
        res.append(Coords(self.x, self.y+1))
        res.append(Coords(self.x-1, self.y))
        return res

    def egal(self, c):
        return self.x == c.x and self.y == c.y

    def __repr__(self):
        return ("Case " + str(self.x) + ' | ' + str(self.y))


class Joueur:
    def __init__(self, xmax, ymax, dir):
        self.xmax = xmax
        self.ymax = ymax
        infos = self.read()
        self.carte = infos[2]
        self.pos = Coords(infos[1], infos[0])
        self.dir = self.direct(dir)
        self.mouv = ["UP", "RIGHT", "DOWN", "LEFT"]

    def __repr__(self):
        return ("On map " + str(self.xmax) + "x" + str(self.ymax) + " on pos: " + str(self.pos))

    def direct(self, dir):
        if dir == 'UP':
            return 0
        if dir == 'RIGHT':
            return 1
        if dir == 'DOWN':
            return 2
        return 3

    def case(self, c):
        return self.carte[c.y][c.x]

    def inmap(self, c):
        return 0 <= c.x and c.x < self.xmax and 0 <= c.y and c.y < self.ymax

    def obstacle(self, c, nope):
        for i in nope:
            if self.case(c) == i:
                return True
        return False

    def read(self):
        infos = []
        carte = []
        y, x = [int(i) for i in input().split()]
        infos.append(y)
        infos.append(x)
        for i in range(self.ymax):
            row = input()
            carte.append(row)
        infos.append(carte)
        return infos

    def update(self):
        infos = self.read()
        self.carte = infos[2]
        self.pos = Coords(infos[1], infos[0])

    def move(self, cible, nope, vu):
        for i in self.carte:
            log(i)
        prec = [[-1 for i in range(self.xmax)] for j in range(self.ymax)]
        queue = []
        queue.append(self.pos)
        while len(queue) > 0 and self.case(queue[0]) != cible:
            voi = queue.pop(0).voinsins()
            for i in range(len(voi)):
                n = voi[i]
                if self.inmap(n) and self.obstacle(n, nope) is False and prec[n.y][n.x] == -1:
                    prec[n.y][n.x] = (i+2) % 4
                    queue.append(n)

        if (len(queue) == 0):
            return False
        # for i in prec:
        #   log(i)
        else:
            destination = queue.pop(0)
            chemin = []
            iter = destination
            while (iter.egal(self.pos) is False):
                chemin.append((prec[iter.y][iter.x]+2) % 4)
                iter = iter.voinsins()[prec[iter.y][iter.x]]
            log(chemin)

            while ((vu and self.case(destination) == cible) or (vu is False and len(chemin) > 0)):
                print(self.mouv[chemin.pop(-1)])
                self.update()
            return True


# ymax: number of rows.
# xmax: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
ymax, xmax, a = [int(i) for i in input().split()]
kirk = Joueur(xmax, ymax, 'UP')
# game loop
while True:
    nope = ['#', 'C']
    while (kirk.move('?', nope, True) is False):
        obstacles = ['#', '?']
        kirk.move('C', obstacles, False)
        kirk.move('T', obstacles, False)
