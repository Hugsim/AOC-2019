from typing import Tuple
from lib import *
from intcode import *

initialData: [int] = mapList(toInt, fileIntoArray("data17.txt")[0].split(","))
initialData[0] = 2

comp = IntcodeComputer(initialData)

inp = []
while (res := comp.runUntilInput(inp)) is not None and res != "HLT":
    try:
        asciiPrint(res)
    except:
        break
    inp = maplist(ord, input("λ ")) + [10]
    print(f"Input: {inp}")

print(res)

# Part 1
# result = list(filter(lambda r: len(r) > 0, "".join(map(toChr, result)).split("\n")))
# crossings = []
# for i in range(1, len(result) - 1):
#     for j in range(1, len(result[i]) - 1):
#         if (
#             result[i][j] == "#"
#             and result[i][j - 1] == "#"
#             and result[i][j + 1] == "#"
#             and result[i - 1][j] == "#"
#             and result[i + 1][j] == "#"
#         ):
#             crossings.append((i, j))


"""
A:
L,12,R,8,L,6,R,8,L,6

B:
R,8,L,12,L,12,R,8

C:
L,6,R,6,L,12

"""


"""
A,B,A,A,B,C,B,C,C,B
"""
