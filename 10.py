from typing import Tuple
from lib import *
import math

data = mapList(lambda row: row[:-1], fileIntoArray("data10.txt"))

height = len(data)
width = len(data[0])


def isAsteroid(coords: Tuple[int, int]) -> bool:
    return data[snd(coords)][fst(coords)] == '#'


allAsteroidCoords: Tuple[int, int] = []

for i, row in enumerate(data):
    for j, elem in enumerate(row):
        if isAsteroid((i, j)):
            allAsteroidCoords.append((i, j))


def isVisible(origin: Tuple[int, int], dest: Tuple[int, int]) -> bool:
    yDiff = fst(dest) - fst(origin)
    xDiff = snd(dest) - snd(origin)
    for n in range(1, max(abs(xDiff), abs(yDiff))+1):
        if (xDiff % n == 0) and (yDiff % n == 0):
            stepSizeX = int(xDiff / n)
            stepSizeY = int(yDiff / n)
            for m in range(1, n):
                coord = (m * stepSizeY + fst(origin),
                         m * stepSizeX + snd(origin))
                if isAsteroid(coord):
                    return False
    return True


def visibleFrom(coords: Tuple[int, int]) -> [int]:
    result = []
    for other in allAsteroidCoords:
        if other == coords:
            continue
        if isVisible(coords, other):
            result.append(other)
    return result


def numVisibleFrom(coords: Tuple[int, int]) -> int:
    return len(visibleFrom(coords))


results = []
for i, asteroid in enumerate(allAsteroidCoords):
    print(f"Calculating asteroid at coordinates {asteroid}")
    results.append((asteroid, numVisibleFrom(asteroid)))

results = sorted(results, key=snd, reverse=True)

best = results[0][0]
print(best)


def sortFunc(origin: Tuple[int, int], coords: Tuple[Tuple[int, int], int]) -> float:
    return -math.atan2(coords[0] - origin[0], coords[1] - origin[1])


newResults = []

destroyed = sorted(visibleFrom(best), key=(lambda v: sortFunc(best, v)))
print(destroyed)
print(destroyed[0], destroyed[1], destroyed[2], destroyed[9],
      destroyed[19], destroyed[49], destroyed[99], destroyed[199])

n = numVisibleFrom
