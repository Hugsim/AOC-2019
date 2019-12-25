import numpy as np
from typing import Tuple
from lib import *
import math


def cmpPos(pos1, pos2):
    return np.sign(pos2 - pos1)


def potentialEnergy(pos):
    return sum(map(abs, pos))


def kineticEnergy(vel):
    return sum(map(abs, vel))


moonPos = mapList(
    lambda l: np.array(
        mapList(toInt, l[:-1].split(" "))), fileIntoArray("data12.txt"))


def simulateUntilRepeat(p1, p2, p3, p4):
    initialState = [p1, p2, p3, p4]
    vels = [0, 0, 0, 0]
    t = 1
    curState = initialState.copy()

    while True:
        if t % 10_000 == 0:
            print(t)

        for i in range(4):
            for j in range(i):
                acc = cmpPos(curState[i], curState[j])
                vels[i] += acc
                vels[j] -= acc

        for i in range(4):
            curState[i] += vels[i]

        t += 1

        if curState == initialState:
            break

    return t


xRep = simulateUntilRepeat(*mapList(lambda x: x[0], moonPos))
print(xRep)
yRep = simulateUntilRepeat(*mapList(lambda x: x[1], moonPos))
print(yRep)
zRep = simulateUntilRepeat(*mapList(lambda x: x[2], moonPos))
print(zRep)

print(f"lcm({xRep}, {yRep}, {zRep})")

# Numpy lcm() doesn't work properly, probably overflows somewhere
print(np.lcm.reduce([xRep, yRep, zRep]))
