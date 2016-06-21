#!/usr/bin/env python3

size = (0, 0)
zombies = list()

def importFromFile(filename):
    global size
    with open(filename, 'r') as f:
        text = f.read()

    text = text.rstrip()
    lines = text.split('\n')

    size = (lines[0].split())

    for x in lines[1:]:
        zombies.append(tuple(x.split()))

    # Create map
    printMap = False
    if printMap:
        for c in range(0, int(size[0])):
            line = ['.'] * int(size[1])
            zombsOnLine = [z for z in zombies if int(z[0]) == c]
            for z in zombsOnLine:
                line[int(z[1])] = 'X'
                #print("Yes!")
            print("".join(line))

    # End Debug

def _hit(shot, pos):
    if int(shot[0]) >= int(pos[0]) - 1 and \
       int(shot[0]) <= int(pos[0]) + 1 and \
       int(shot[1]) >= int(pos[1]) - 1 and \
       int(shot[1]) <= int(pos[1]) + 1:
        return True
    return False

def findOptimalShot():
    global size

    bestShotKills = -1


    bestShotDir = (-1, -1)
    bestCoords = []

    vertCount = 0
    count = 0
    lrDiaCount = 0
    rlDiaCount = 0
    # Search vertically
    print ("For in range... " + str(size) + " : " + str(len(zombies)))

    # TODO: Optimise this, please
    # Horizontally

    print ("horz")
    for x in range (0, int(size[0])):
        # New shot
        count = 0
        shotZombies = []
        testedCoords = []

        for y in range(0, int(size[1])):
            testedCoords.append((x, y))
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (x, 0)
                bestCoords = testedCoords

    # Vertically
    print ("vert")
    for y in range (0, int(size[1])):
        # New shot
        count = 0
        shotZombies = []
        testedCoords = []

        for x in range(0, int(size[0])):
            testedCoords.append((x, y))
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (0, y)
                bestCoords = testedCoords

    # 0.0, 1.1, 2.2, 3.3
    # Diagonally d-l-r
    '''
    X.....X...
    ..........
    ....X.....
    ..........
    ......X...
    .....X....
    '''

    print ("dlr")
    for col in range (0, int(size[0])):
        # New shot
        count = 0
        shotZombies = []
        testedCoords = []

        # Don't use double for...
        y = 0
        for x in range (col, int(size[0])):
            testedCoords.append((x, y))
            #for y in range(0, int(size[1])):
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (col, 1)
                bestCoords = testedCoords
            y += 1
            if y >= int(size[1]):
                break

    print("drl")
    for col in range (int(size[0]) - 1, -1, -1):
        # New shot
        count = 0
        shotZombies = []
        testedCoords = []

        # Don't use double for...
        y = 0
        for x in range (col, -1, -1):
            testedCoords.append((x, y))
            #for y in range(0, int(size[1])):
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    #print (str(x) + ":" + str(y) + " killed " + str(z))
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (col, 1)
                bestCoords = testedCoords
            y += 1
            if y >= int(size[1]):
                break

    # Create map
    printMap = False
    if printMap:
        for c in range(0, int(size[0])):
            line = ['.'] * int(size[1])
            zombsOnLine = [z for z in zombies if int(z[0]) == c]
            for z in zombsOnLine:
                line[int(z[1])] = 'X'
                #print("Yes!")
            coordsOnLine = [p for p in bestCoords if int(p[0]) == c]
            for p in coordsOnLine:
                line[int(p[1])] = '#'
            print("".join(line))


    print ("BestShotKills: " + str(bestShotKills) + ", BestShotDirection: " + str(bestShotDir[0]) + ":" + str(bestShotDir[1]))


if __name__ == '__main__':
    importFromFile("./input")
    findOptimalShot()
