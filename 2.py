import typing
from lib import *

initialData: [int] = list(map(toInt, fileIntoArray("data2.txt")[0].split(",")))


def findInputs(program: [int], goal: int) -> (int, int):
    for in1 in range(0, 100):
        for in2 in range(0, 100):
            print("Testing " + str((in1, in2)))
            data0 = evalProgram(program.copy(), in1, in2)
            if data0 is goal:
                return (in1, in2)


def evalProgram(program: [int], in1: int, in2: int) -> int:
    # print(program)
    PC = 0
    program[1] = in1
    program[2] = in2
    while True:
        inst = program[PC]
        try:
            loc1 = program[PC+1]
            loc2 = program[PC+2]
            dest = program[PC+3]
        except:
            print("bad")
            loc1 = -1
            loc2 = -1
            dest = -1
        # print("inst: " + str(inst) + " loc1: " + str(loc1) +
        #      " loc2: " + str(loc2) + " dest: " + str(dest))
        if inst is 1:
            program[dest] = program[loc1] + program[loc2]
        elif inst is 2:
            program[dest] = program[loc1] * program[loc2]
        elif inst is 99:
            print("Result: " + str(program[0]))
            return program[0]
        PC += 4
        #print("PC: " + str(PC))


print(findInputs(initialData, 19690720))
