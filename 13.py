from typing import Tuple
from lib import *
from intcode import *
import os

def fancyPrint(arr):
    os.system("cls")
    print(f"Score: {lastScore}")
    for row in arr:
        for tile in row:
            print(tile, end="")
        print("")


EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

TILE_CHARACTERS = [" ", "\u2588", "\u2592", "\u2580", "\u25cb"]

initialData: [int] = mapList(toInt, fileIntoArray("data13.txt")[0].split(","))
initialData[0] = 2

comp = IntcodeComputer(initialData)
outputs = []

playingField = []
for i in range(24):
    playingField.append([TILE_CHARACTERS[EMPTY]] * 37)

lastScore = 0

outputCounter = 0

while (res := comp.runUntilOutput(auto=True)) is not None:
    if res == "HLT":
        break
    elif res == "INP":
       _, ballPos = find2d(playingField, TILE_CHARACTERS[BALL])
       _, paddlePos = find2d(playingField, TILE_CHARACTERS[PADDLE])
       comp.addInput(-1 if paddlePos > ballPos else (0 if paddlePos == ballPos else 1))
       fancyPrint(playingField)
       continue

    outputs.append(res)
    outputCounter += 1
    if outputCounter == 3:
        outputCounter = 0
        tile = tuple(outputs[-3:])
        if fst(tile) == -1 and snd(tile) == 0:
            lastScore = trd(tile)
        else:           
            playingField[snd(tile)][fst(tile)] = TILE_CHARACTERS[trd(tile)]

print(lastScore)

# Part 1
# print(len(list(filter(lambda pair: trd(pair) == BLOCK, tiles))))
