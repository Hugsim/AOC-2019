from lib import *
import typing

def pointPlus(p1: (int, int), p2: (int, int)) -> (int, int):
    return (p1[0] + p2[0], p1[1] + p2[1])


def loopThroughListAndAddPositions(dirs: [(str, int)]) -> [(int, int)]:
    resList = [(0, 0)]
    curPoint = (0, 0)
    for (direction, amount) in dirs:
        if direction == "U":
            for i in range(1, amount):
                resList.append(pointPlus(curPoint, (0, i)))
            curPoint = pointPlus(curPoint, (0, amount))
            resList.append(curPoint)
        elif direction == "D":
            for i in range(1, amount):
                resList.append(pointPlus(curPoint, (0, -i)))
            curPoint = pointPlus(curPoint, (0, -amount))
            resList.append(curPoint)
        elif direction == "L":
            for i in range(1, amount):
                resList.append(pointPlus(curPoint, (-i, 0)))
            curPoint = pointPlus(curPoint, (-amount, 0))
            resList.append(curPoint)
        elif direction == "R":
            for i in range(1, amount):
                resList.append(pointPlus(curPoint, (i, 0)))
            curPoint = pointPlus(curPoint, (amount, 0))
            resList.append(curPoint)

    return resList


def manhattanDistanceFromCentre(p: (int, int)) -> int:
    return abs(p[0]) + abs(p[1])


c1, c2 = mapList(lambda l: mapList(lambda x: (x[0], int(x[1:])), l), map(
    lambda x: x.strip("\n").split(","), fileIntoArray("data3.txt")))

visited1 = loopThroughListAndAddPositions(c1)
visited2 = loopThroughListAndAddPositions(c2)

visited1Set = set(visited1)
visited2Set = set(visited2)

visited1In2 = [p for p in visited1 if p in visited2Set]
visited2In1 = [p for p in visited2 if p in visited1Set]

visited1WithDistances = [(p, visited1.index(p)) for p in visited1In2]
visited2WithDistances = [(p, visited2.index(p)) for p in visited2In1]

pointsWithDistances = [(p1[0], p1[1] + p2[1])
                       for p1 in visited1WithDistances for p2 in visited2WithDistances if p1[0] == p2[0]]

distances = filter(lambda p: p != 0, mapList(snd, pointsWithDistances))
print(min(list(distances)))
