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

    # Debug
    print ("Size: " + str(size[0]) + " : " + str(size[1]))
    for z in zombies:
        print ("Zom" + ": " + str(z[0]) + " : " + str(z[1]))

    '''
    X.....X...
    ..........
    ....X.....
    ..........
    ......X...
    .....X....

    X.....X...
    ..........
    ....X.....
    ..........
    ......X...
    .....X....

    '''

    # Create map
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
    print("Opt")

    '''
    X.....X...
    ..........
    ....X.....
    ..........
    ......X...
    .....X....
    '''

    bestShotKills = -1
    bestShotDir = (-1, -1)

    vertCount = 0
    count = 0
    lrDiaCount = 0
    rlDiaCount = 0
    # Search vertically
    print ("For in range... " + str(size) + " : " + str(len(zombies)))

    # Optimise this, please
    # Horizontally
    print ("horz")
    for x in range (0, int(size[0])):
        # New shot
        count = 0
        shotZombies = []

        for y in range(0, int(size[1])):
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (x, 0)

    # Vertically
    print ("vert")
    for y in range (0, int(size[1])):
        # New shot
        count = 0
        shotZombies = []

        for x in range(0, int(size[0])):
            for z in zombies:
                if _hit(z, (x, y)) and not z in shotZombies:
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (0, y)

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
        print("reset")

        # Don't use double for...
        for x in range (col, int(size[0])):
            for y in range(0, int(size[1])):
                for z in zombies:
                    if _hit(z, (x, y)) and not z in shotZombies:
                        print (str(x) + ":" + str(y) + " killed " + str(z))
                        count += 1
                        shotZombies.append(z)
                if count > bestShotKills:
                    bestShotKills = count
                    bestShotDir = (col, 1)
                    print("Zombies")
                    print(str(shotZombies))

    '''
    # Diagonally d-r-l
    for x in range (0, int(size[1])):
        # New shot
        print ("Reset")
        count = 0
        shotZombies = []

        for y in range(0, int(size[0])):
            for z in zombies:
                if _hit(z, (y, x)) and not z in shotZombies:
                    print("HIT!")
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (x, y)

    # Diagonally u-l-r
    for x in range (0, int(size[1])):
        # New shot
        print ("Reset")
        count = 0
        shotZombies = []

        for y in range(0, int(size[0])):
            for z in zombies:
                if _hit(z, (y, x)) and not z in shotZombies:
                    print("HIT!")
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (x, y)

    # Diagonally u-r-l
    for x in range (0, int(size[1])):
        # New shot
        print ("Reset")
        count = 0
        shotZombies = []

        for y in range(0, int(size[0])):
            for z in zombies:
                if _hit(z, (y, x)) and not z in shotZombies:
                    print("HIT!")
                    count += 1
                    shotZombies.append(z)
            if count > bestShotKills:
                bestShotKills = count
                bestShotDir = (x, y)

    '''
    print ("BestShotKills: " + str(bestShotKills) + ", BestShotDirection: " + str(bestShotDir[0]) + ":" + str(bestShotDir[1]))

        # Search horizontally
        #

    # Search vertically
    # Search diagonally l-r
    # Search diagonally r-l

if __name__ == '__main__':
    importFromFile("./input")
    findOptimalShot()
