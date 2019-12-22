from typing import Any
from lib import *

# 2028 Too high

data = fileIntoArray("data8.txt")[0]

WIDTH = 25
HEIGHT = 6

BLACK = 0
WHITE = 1
TRANSPARENT = 2

BLOCKS = ['\u2591', '\u2588']


def chunk(l: [Any], n: int) -> [[Any]]:
    return [l[i:i + n] for i in range(0, len(l), n)]


layers: [[int]] = chunk(mapList(toInt, data), WIDTH*HEIGHT)

# layers.sort(key=lambda l: l.count(0))

# print(layers[0].count(1) * layers[0].count(2))

output = []

for h in range(HEIGHT):
    output.append([])
    for w in range(WIDTH):
        i = h * WIDTH + w
        for layer in layers:
            if layer[i] != TRANSPARENT:
                output[h].append(BLOCKS[layer[i]])
                print(BLOCKS[layer[i]], end="")
                break
    print("")
