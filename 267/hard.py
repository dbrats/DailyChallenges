#!/usr/bin/env python3

from collections import defaultdict

# Globals
size = (0, 0)
zombies = list()
comparisons = 0


def _hit(shot, pos):
    global comparisons
    comparisons += 1
    if int(shot[0]) >= int(pos[0]) - 1 and \
       int(shot[0]) <= int(pos[0]) + 1 and \
       int(shot[1]) >= int(pos[1]) - 1 and \
       int(shot[1]) <= int(pos[1]) + 1:
        return True
    return False


def _printMap():
    # Create map
    for c in range(0, int(size[0])):
        line = ['.'] * int(size[1])
        zombsOnLine = [z for z in zombies if int(z[0]) == c]
        for z in zombsOnLine:
            line[int(z[1])] = 'X'
            #print("Yes!")
        print("".join(line))


def importFromFile(filename):
    global size
    with open(filename, 'r') as f:
        text = f.read()

    text = text.rstrip()
    lines = text.split('\n')
    size = (lines[0].split())

    for x in lines[1:]:
        zombies.append(tuple(x.split()))

    debugMap = True
    if debugMap:
        _printMap()


def findOptimalShot():
    global size

    bestShotKills = -1

    # Search vertically
    print ("For in range... " + str(size) + " : " + str(len(zombies)))
    loops = 0
    zombieLines = defaultdict(lambda: 0)
    for z in zombies:
        loops += 1
        x = int(z[0])
        y = int(z[1])

        # TODO: Optimise this code, split into functions, and less dict lookups.
        zombieLines[(1, x)] += 1
        zombieLines[(1, x-1)] += 1
        zombieLines[(1, x+1)] += 1
        zombieLines[(2, y)] += 1
        zombieLines[(2, y-1)] += 1
        zombieLines[(2, y+1)] += 1
        zombieLines[(3, y-x)] += 1
        zombieLines[(3, y-x+1)] += 1
        zombieLines[(3, y-x-1)] += 1
        zombieLines[(4, y+x)] += 1
        zombieLines[(4, y+x+1)] += 1
        zombieLines[(4, y+x-1)] += 1

        if zombieLines[(1, x)] > bestShotKills:
            bestShotKills = zombieLines[(1, x)]
        elif zombieLines[(1, x-1)] > bestShotKills:
            bestShotKills = zombieLines[(1, x-1)]
        elif zombieLines[(1, x+1)] > bestShotKills:
            bestShotKills = zombieLines[(1, x+1)]
        elif zombieLines[(2, y)] > bestShotKills:
            bestShotKills = zombieLines[(2, y)]
        elif zombieLines[(2, y-1)] > bestShotKills:
            bestShotKills = zombieLines[(2, y-1)]
        elif zombieLines[(2, y+1)] > bestShotKills:
            bestShotKills = zombieLines[(2, y+1)]
        elif zombieLines[(3, y-x)] > bestShotKills:
            bestShotKills = zombieLines[(3, y-x)]
        elif zombieLines[(3, y-x-1)] > bestShotKills:
            bestShotKills = zombieLines[(3, y-x-1)]
        elif zombieLines[(3, y-x+1)] > bestShotKills:
            bestShotKills = zombieLines[(3, y-x+1)]
        elif zombieLines[(4, y+x)] > bestShotKills:
            bestShotKills = zombieLines[(4, y+x)]
        elif zombieLines[(4, y+x-1)] > bestShotKills:
            bestShotKills = zombieLines[(4, y+x-1)]
        elif zombieLines[(4, y+x+1)] > bestShotKills:
            bestShotKills = zombieLines[(4, y+x+1)]


    print ("BestShotKills: " + str(bestShotKills))
    print ("Loops: " + str(loops))


if __name__ == '__main__':
    importFromFile("./input")
    findOptimalShot()
    print ("Comparisons: " + str(comparisons))
