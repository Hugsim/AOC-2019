from typing import Any
from lib import *


class IntcodeComputer:
    def __init__(self, program, inputs=[]):
        self.program = program + ([0] * 1_000_000)
        self.inputs = inputs

    def runUntilOutput(self, inputs=[], debug=False, auto=False):
        for i in inputs:
            self.inputs.append(i)
        return evalProgramUntilOutput(self.program, self.inputs, debug, auto)

    def addInput(self, inp):
        self.inputs.append(inp)


def printIf(val: Any, predicate: bool):
    if predicate:
        print(val)


def getOpcodeModes(numOpcodes: int, fullOpcode: int) -> [int]:
    paddedNumber = f'{fullOpcode:0{numOpcodes + 2}}'
    return mapList(toInt, paddedNumber[0:numOpcodes])[::-1]


PC = 0
IC = 0
RB = 0


def evalProgramUntilOutput(program: [int], inputs: [int] = [], debug: bool = False, auto: bool = False):
    global PC
    global IC
    global RB
    while True:
        fullInst = program[PC]
        inst = int(str(fullInst)[-2:])
        printIf(f"fullInst={fullInst}, inst={inst}", debug)

        if inst == 1:
            printIf("ADD", debug)
            val1 = -1337
            val2 = -1337
            dest = -1

            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            printIf(f"opcodeModes={opcodeModes}, arguments={args}", debug)

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                printIf(f"Got 1st value {val1} from address {args[0]}", debug)
            elif opcodeModes[0] == 1:
                val1 = args[0]
            elif opcodeModes[0] == 2:
                val1 = program[args[0] + RB]
                printIf(
                    f"Got 1st value {val1} from address {args[0] + RB} via RB", debug)

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]
            elif opcodeModes[1] == 2:
                val2 = program[args[1] + RB]
                printIf(
                    f"Got 2nd value {val2} from address {args[1] + RB} via RB", debug)

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break
            elif opcodeModes[2] == 2:
                dest = args[2] + RB

            printIf(f"Adding together {val1} and {val2}", debug)
            printIf(f"Writing {val1 + val2} to address {dest}", debug)
            program[dest] = val1 + val2
            PC += 4

        elif inst == 2:
            printIf("MUL", debug)
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            printIf(f"opcodeModes={opcodeModes}, arguments={args}", debug)

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                printIf(f"Got 1st value {val1} from address {args[0]}", debug)
            elif opcodeModes[0] == 1:
                val1 = args[0]
            elif opcodeModes[0] == 2:
                val1 = program[args[0] + RB]
                printIf(
                    f"Got 1st value {val1} from address {args[0] + RB} via RB", debug)

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]
            elif opcodeModes[1] == 2:
                val2 = program[args[1] + RB]
                printIf(
                    f"Got 2nd value {val2} from address {args[1] + RB} via RB", debug)

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break
            elif opcodeModes[2] == 2:
                dest = args[2] + RB

            printIf(f"Writing {val1 * val2} to address {dest}", debug)
            program[dest] = val1 * val2
            PC += 4

        elif inst == 3:
            printIf("INP", debug)
            arg = program[PC+1]
            opcodeModes = getOpcodeModes(1, fullInst)
            userInput = -1337
            if IC < len(inputs):
                userInput = inputs[IC]
                printIf(
                    f"Inputting {userInput} automatically when PC={PC}", debug)
                IC += 1
            else:
                if auto:
                    return "INP"
                else:
                    userInput = int(input(f'Input requested when PC={PC}: '))

            if opcodeModes[0] == 0:
                printIf(f"Writing {userInput} to address {arg}", debug)
                program[arg] = userInput
            elif opcodeModes[0] == 2:
                printIf(
                    f"Writing {userInput} to address {arg + RB} via RB.", debug)
                program[arg + RB] = userInput
            else:
                printIf(f'This should never happen! PC={PC}', debug)
                break

            PC += 2

        elif inst == 4:
            printIf("OUT", debug)
            toprint = -1337
            arg = program[PC+1]
            mode = getOpcodeModes(1, fullInst)[0]

            if mode == 0:
                printIf(f"Outputting value at adress {arg}.", debug)
                toprint = program[arg]
            elif mode == 1:
                printIf(f"Outputting immediate value {arg}.", debug)
                toprint = arg
            elif mode == 2:
                printIf(
                    f"Outputting value at adress {arg + RB} via RB.", debug)
                toprint = program[arg + RB]

            printIf(f'Output at PC={PC}: {toprint}', debug)
            PC += 2
            return toprint

        elif inst == 5:
            printIf("JNZ", debug)
            args = program[PC+1:PC+3]
            opcodeModes = getOpcodeModes(2, fullInst)
            jumpTarget = -1337
            if opcodeModes[1] == 0:
                jumpTarget = program[args[1]]
            elif opcodeModes[1] == 1:
                jumpTarget = args[1]
            elif opcodeModes[1] == 2:
                jumpTarget = program[args[1] + RB]

            if opcodeModes[0] == 0:
                if program[args[0]] != 0:
                    printIf(
                        f"Value at address {args[0]} was {program[args[0]]}, not 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address {args[0]} was 0. Not jumping.", debug)

            elif opcodeModes[0] == 1:
                if args[0] != 0:
                    printIf(
                        f"Immediate value {args[0]} is not 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address {args[0]} was 0. Not jumping.", debug)
            elif opcodeModes[0] == 2:
                if program[args[0] + RB] != 0:
                    printIf(
                        f"Value at address (via RB) {args[0] + RB} was {program[args[0] + RB]}, not 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address (via RB) {args[0] + RB} was 0. Not jumping.", debug)

            PC += 3

        elif inst == 6:
            printIf("JIZ", debug)
            arg = program[PC+1:PC+3]
            opcodeModes = getOpcodeModes(2, fullInst)
            jumpTarget = -1337
            if opcodeModes[1] == 0:
                jumpTarget = program[arg[1]]
            elif opcodeModes[1] == 1:
                jumpTarget = arg[1]
            elif opcodeModes[1] == 2:
                jumpTarget = program[arg[1] + RB]

            if opcodeModes[0] == 0:
                if program[arg[0]] == 0:
                    printIf(
                        f"Value at address {arg[0]} was 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address {arg[0]} was {program[arg[0]]}, not 0. Not jumping.", debug)
            elif opcodeModes[0] == 1:
                if arg[0] == 0:
                    printIf(
                        f"Immediate value {arg[0]} was 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address {arg[0]} was not 0. Not jumping.", debug)
            elif opcodeModes[0] == 2:
                if program[arg[0] + RB] == 0:
                    printIf(
                        f"Value at address (via RB) {arg[0] + RB} was 0. Jumping to {jumpTarget}.", debug)
                    PC = jumpTarget
                    continue
                else:
                    printIf(
                        f"Value at address (via RB) {arg[0] + RB} was {program[arg[0] + RB]}, not 0. Not jumping.", debug)

            PC += 3

        elif inst == 7:
            printIf("LTH", debug)
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            printIf(f"opcodeModes={opcodeModes}, arguments={args}", debug)

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                printIf(f"Got 1st value {val1} from address {args[0]}", debug)
            elif opcodeModes[0] == 1:
                val1 = args[0]
            elif opcodeModes[0] == 2:
                val1 = program[args[0] + RB]
                printIf(
                    f"Got 1st value {val1} from address {args[0] + RB} via RB", debug)

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]
            elif opcodeModes[1] == 2:
                val2 = program[args[1] + RB]
                printIf(
                    f"Got 2nd value {val2} from address {args[1] + RB} via RB", debug)

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break
            elif opcodeModes[2] == 2:
                dest = args[2] + RB

            program[dest] = 1 if val1 < val2 else 0
            PC += 4

        elif inst == 8:
            printIf("EQU", debug)
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            printIf(f"opcodeModes={opcodeModes}, arguments={args}", debug)

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                printIf(f"Got 1st value {val1} from address {args[0]}", debug)
            elif opcodeModes[0] == 1:
                val1 = args[0]
            elif opcodeModes[0] == 2:
                val1 = program[args[0] + RB]
                printIf(
                    f"Got 1st value {val1} from address {args[0]} via RB", debug)

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]
            elif opcodeModes[1] == 2:
                val2 = program[args[1] + RB]
                printIf(
                    f"Got 2nd value {val2} from address {args[1] + RB} via RB", debug)

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break
            elif opcodeModes[2] == 2:
                dest = args[2] + RB

            program[dest] = 1 if val1 == val2 else 0
            PC += 4

        elif inst == 9:
            printIf("ARB", debug)
            val = -1337
            args = program[PC+1:PC+2]
            opcodeModes = getOpcodeModes(1, fullInst)
            printIf(f"opcodeModes={opcodeModes}, arguments={args}", debug)

            if opcodeModes[0] == 0:
                val = program[args[0]]
                printIf(f"Got value {val1} from address {args[0]}", debug)
            elif opcodeModes[0] == 1:
                val = args[0]
            elif opcodeModes[0] == 2:
                val = program[args[0] + RB]

            RB += val
            PC += 2

        elif inst == 99:
            printIf("HLT", debug)
            printIf(f'Program halted when PC={PC}', debug)
            return "HLT"

        else:
            printIf(
                f"Trying to do an illegal operation: {inst} at PC={PC}.", debug)
            break
