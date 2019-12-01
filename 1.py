import typing
import math as m
from lib import *


def fuelNeeded(weight: int) -> int:
    return m.floor(weight/3) - 2


def fuelNeededSmart(weight: int) -> int:
    totalFuel: int = 0
    fuelReq: int = fuelNeeded(weight)
    while fuelReq > 0:
        totalFuel += fuelReq
        fuelReq = fuelNeeded(fuelReq)
    return totalFuel


print(sum(map(fuelNeededSmart, map(lambda x: int(x), fileIntoArray("data1.txt")))))
