#!/usr/bin/env python3

import random
from collections import defaultdict

# Ingests text to store in memory for random text generation.
def ingest(filename):
    print ('Ingesting text...')

    with open(filename, 'r') as f:
        text = f.read()

    # Split on space
    words = text.split()

    memory = defaultdict(list)
    count = 0

    for x in words:
        # NONWORD signals point of entry for the text generating algorithm
        if count - 1 < 0:
            key = 'NONWORD NONWORD'
        elif count - 2 < 0:
            key = 'NONWORD ' + str(words[count - 1])
        else:
            key = str(words[count-2] + ' ' + words[count-1])
        memory[key].append(x)
        count += 1

    print ('Ingested ' + str(count) + ' words.')

    # 'NONWORD' signals the end of the text being generated
    key = str(words[-2] + ' ' + words[-1])
    memory[key].append('NONWORD')

    return memory


# Generates random text based on memory
def generate(memory):
    words = []

    # NONWORDs signals the start of text being generated
    key = 'NONWORD NONWORD'
    words.append(memory[key][0])

    key = 'NONWORD ' + str(words[0])
    nextword = memory[key][0]

    while nextword != 'NONWORD': # Not a NONWORD
        words.append(nextword)
        key = str(words[-2]) + ' ' + str(words[-1])
        nextword = random.choice(memory[key])

    text = ''
    for x in words:
        text = text + x + ' '
        # TODO: Calculate the average length of line/paragraphs and add line breaks.

    print('\n\nOutput:\n' + text)


if __name__ == '__main__':
    filename = './badromance.txt'
    memory = ingest(filename)
    generate(memory)
