from typing import Any
from lib import *


def printIf(val: Any, predicate: bool):
    if predicate:
        print(val)


def getOpcodeModes(numOpcodes: int, fullOpcode: int) -> [int]:
    paddedNumber = f'{fullOpcode:0{numOpcodes + 2}}'
    return mapList(toInt, paddedNumber[0:numOpcodes])[::-1]


def evalProgram(program: [int], inputs: [int], debug: bool = False):
    PC = 0
    IC = 0
    output: [int] = []
    print(inputs)
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

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break

            printIf(f"Adding together {val1} and {val2}.", debug)
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

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break
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
                userInput = int(input(f'Input requested when PC={PC}: '))
            if opcodeModes[0] == 0:
                printIf(f"Writing {userInput} to address {arg}", debug)
                program[arg] = userInput
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
            output.append(toprint)
            printIf(f'Output at PC={PC}: {toprint}', debug)
            PC += 2

        elif inst == 5:
            printIf("JNZ", debug)
            args = program[PC+1:PC+3]
            opcodeModes = getOpcodeModes(2, fullInst)
            jumpTarget = -1337
            if opcodeModes[1] == 0:
                jumpTarget = program[args[1]]
            elif opcodeModes[1] == 1:
                jumpTarget = args[1]

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

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break

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

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                printIf(f"Got 2nd value {val2} from address {args[1]}", debug)
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                printIf(f'This should never happen! PC={PC}', debug)
                break

            program[dest] = 1 if val1 == val2 else 0
            PC += 4

        elif inst == 99:
            printIf("HLT", debug)
            printIf(f'Program halted when PC={PC}', debug)
            return output

        else:
            printIf(
                f"Trying to do an illegal operation: {inst} at PC={PC}.", debug)
            printIf(f"Was going to output {output}.", debug)
            break
