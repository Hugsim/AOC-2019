import typing
from lib import *
from intcode import evalProgram
import itertools

initialData: [int] = mapList(toInt, fileIntoArray("data7.txt")[0].split(","))
inputs: [[int]] = mapList(toList, itertools.permutations(range(5)))

# Test program
# initialData = [3, 15,             # INP 15          ; phase -> 15
#                3, 16,             # INP 16          ; input -> 16
#                1002, 16, 10, 16,  # MUL 16, #10, 16 ; input * 10 -> 16
#                1, 16, 15, 15,     # ADD 16, 15, 15  ; 16 + phase -> output
#                4, 15,             # OUT 15          ; return output
#                99,                # HLT             ; break
#                0,                 # 15
#                0]                 # 16

#inputs: [int] = [[9, 8, 7, 6, 5]]
outputs: [int] = []

# Part 1
for i in inputs:
    print(f"Trying order {i}:")
    output = evalProgram(initialData.copy(), [i[0], 0])
    print(output)
    output = output[0]
    for j in i[1::]:
        output = evalProgram(initialData.copy(), [j, output])
        print(output)
        output = output[0]
    print(f"Got output {output}")
    outputs.append(output)


print(max(outputs))
# evalProgram(initialData)
