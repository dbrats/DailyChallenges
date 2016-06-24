#!/usr/bin/env python3

from collections import defaultdict

def _printMap(size, zombies):
    # Create map
    for c in range(0, int(size[0])):
        line = ['.'] * int(size[1])
        zombsOnLine = [z for z in zombies if int(z[0]) == c]
        for z in zombsOnLine:
            line[int(z[1])] = 'X'

        print("".join(line))


def importFromFile(filename):
    with open(filename, 'r') as f:
        text = f.read()

    # Strip unnecessary whitespace and split
    text = text.rstrip()
    lines = text.split('\n')

    size = (lines[0].split())

    zombies = []
    # Add a list of the zombie positions.
    for x in lines[1:]:
        zombies.append(tuple(x.split()))

    # Warning: Don't enable this on big data.
    debugMap = True
    if debugMap:
        _printMap(size, zombies)

    return size, zombies


def findOptimalShot(zombies):
    # Add default count of 0 to all possible zombies.
    possibleShots = defaultdict(lambda: 0)

    for z in zombies:
        x = int(z[0])
        y = int(z[1])

        # IDs of "shots" to increment, id = (type, "shot position")
        # 1 = vertical
        # 2 = horizontal
        # 3 and 4 = diagonal shots
        availableShots = [ (1, x), (1, x-1), (1, x+1) \
                         , (2, y), (2, y-1), (2, y+1) \
                         , (3, y-x), (3, y-x-1), (3, y-x+1) \
                         , (4, y+x), (4, y+x-1), (4, y+x+1)]

        # Loop through all the shots needed to reach this and adjacent positions
        for s in availableShots:
            possibleShots[s] += 1

    # No need to do any comparisons until we have the full data.
    return max(possibleShots.values())


if __name__ == '__main__':
    # Read grid size and zombie positions from the specified file.
    size, zombies = importFromFile("./medium_input")
    print ("Searching grid of size: " + str(size) + ", with " + str(len(zombies)) + " zombies.")

    # Calculate the shot that can kill the most zombies at once.
    bestShot = findOptimalShot(zombies)
    print ("Most zombies that can be killed with a single shot: " + str(bestShot))
