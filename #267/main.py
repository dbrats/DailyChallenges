#!/usr/bin/env python3

def listOtherPositions(pos, lastPos = 101):
    for x in range(1, lastPos):
        if x != pos:
            strX = str(x)
            suffix = 'th'
            if strX.endswith('1') and not strX.endswith('11'):
                suffix = 'st'
            elif strX.endswith('2') and not strX.endswith('12'):
                suffix = 'nd'
            elif strX.endswith('3') and not strX.endswith('13'):
                suffix = 'rd'

            print (strX + suffix)

if __name__ == '__main__':
    pos = 2
    lastPos = 100
    listOtherPositions(pos, lastPos)
