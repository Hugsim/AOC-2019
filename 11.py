from typing import Tuple
from lib import *
from intcode import *

initialData: [int] = mapList(toInt, fileIntoArray("data11.txt")[0].split(","))

WHITE_TILE_CHARACTER = '\u2588'
BLACK_TILE_CHARACTER = '\u2591'

TILE_CHARACTER_LOOKUP = [BLACK_TILE_CHARACTER, WHITE_TILE_CHARACTER]

COLOR_LOOKUP = ["black", "white"]

WHITE_TILE = 1
BLACK_TILE = 0

TURN_LEFT = 0
TURN_RIGHT = 1

TURN_LOOKUP = ["up", "left", "down", "right"]

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

painted = {(0, 0): WHITE_TILE}

turtle = IntcodeComputer(initialData)
curX = 0
curY = 0
facing = 0

debug = False

shouldContinue = True
while shouldContinue:
    if debug:
        input()
    curPos = (curX, curY)
    toInput = painted.get(curPos, 0)
    # print(f"Inputting {toInput} ({COLOR_LOOKUP[toInput]})")
    toPaint = turtle.runUntilOutput([toInput])
    # print(f"Painting {curPos} in {COLOR_LOOKUP[toPaint]}")
    # print(str(painted))
    if toPaint is None:
        break
    if toPaint == WHITE_TILE:
        painted[curPos] = WHITE_TILE
    elif toPaint == BLACK_TILE:
        painted[curPos] = BLACK_TILE

    turn = turtle.runUntilOutput()
    # print(f"Turning to the {TURN_LOOKUP[turn]}")
    if turn is None:
        break
    if turn == TURN_LEFT:
        facing = (facing + 1) % 4
    elif turn == TURN_RIGHT:
        facing = (facing - 1) % 4

    if facing == UP:
        curY += 1
    elif facing == LEFT:
        curX -= 1
    elif facing == DOWN:
        curY -= 1
    elif facing == RIGHT:
        curX += 1

normalized = maplist(lambda p: (
    (fst(fst(p)), snd(fst(p)) + 5), TILE_CHARACTER_LOOKUP[snd(p)]), painted.items())

print(list(filter(lambda p: snd(p) == WHITE_TILE_CHARACTER, normalized)))
