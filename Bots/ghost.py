import sys
import math


def log(x):
    print(x, file=sys.stderr, flush=True)


factory_count = int(input())  # the number of factories
carte = [[30 for i in range(factory_count)] for j in range(factory_count)]
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    carte[factory_1][factory_2] = distance
    carte[factory_2][factory_1] = distance

# game loop
while True:
    myFactoryId = []
    myId = []
    enemyFactoryId = []
    entity_count = int(input())
    # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])

        if entity_type == 'FACTORY':
            if arg_1 == 1:
                myFactoryId.append((arg_2, entity_id))
                myId.append(entity_id)
            elif arg_3 > 0:
                enemyFactoryId.append((arg_2, entity_id))
    myFactoryId.sort()
    enemyFactoryId.sort()
    log(myFactoryId)
    log(enemyFactoryId)
    cmd = ''
    if len(myFactoryId) > 0 and len(enemyFactoryId) > 0:
        cmd = ''
        for i in myFactoryId:
            targets = []
            for j in (enemyFactoryId):
                targets.append(carte[i[1]][j[1]])
            log(targets)
            dest = enemyFactoryId[targets.index(min(targets))][1]
            if i[1] != dest:
                cmd += 'MOVE ' + str(i[1]) + ' ' + str(dest) + ' ' + str(i[0]) + ';'
    if cmd == '':
        cmd = 'WAIT'
    if cmd[-1] == ';':
        print(cmd[:-1])
    else:
        print(cmd)
