import typing
from lib import *

initialData: [int] = list(map(toInt, fileIntoArray("data5.txt")[0].split(",")))


def getOpcodeModes(numOpcodes: int, fullOpcode: int) -> [int]:
    paddedNumber = f'{fullOpcode:0{numOpcodes + 2}}'
    return mapList(toInt, paddedNumber[0:numOpcodes])[::-1]


def evalProgram(program: [int]):
    PC = 0
    while True:
        fullInst = program[PC]
        inst = int(str(fullInst)[-2:])
        print(f"fullInst={fullInst}, inst={inst}")

        if inst == 1:
            print("ADD")
            val1 = -1337
            val2 = -1337
            dest = -1

            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            print(f"opcodeModes={opcodeModes}, arguments={args}")

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                print(f"Got 1st value {val1} from address {args[0]}")
            elif opcodeModes[0] == 1:
                val1 = args[0]

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                print(f"Got 2nd value {val2} from address {args[1]}")
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                print(f'This should never happen! PC={PC}')
                break

            print(f"Writing {val1 + val2} to address {dest}")
            program[dest] = val1 + val2
            PC += 4

        elif inst == 2:
            print("MUL")
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            print(f"opcodeModes={opcodeModes}, arguments={args}")

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                print(f"Got 1st value {val1} from address {args[0]}")
            elif opcodeModes[0] == 1:
                val1 = args[0]

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                print(f"Got 2nd value {val2} from address {args[1]}")
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                print(f'This should never happen! PC={PC}')
                break
            print(f"Writing {val1 * val2} to address {dest}")
            program[dest] = val1 * val2
            PC += 4

        elif inst == 3:
            print("INP")
            arg = program[PC+1]
            opcodeModes = getOpcodeModes(1, fullInst)
            userInput = int(input(f'Input requested when PC={PC}: '))
            if opcodeModes[0] == 0:
                print(f"Writing {userInput} to address {arg}")
                program[arg] = userInput
            else:
                print(f'This should never happen! PC={PC}')
                break
            PC += 2

        elif inst == 4:
            print("OUT")
            toPrint = -1337
            arg = program[PC+1]
            mode = getOpcodeModes(1, fullInst)[0]
            if mode == 0:
                print(f"Outputting value at adress {arg}.")
                toPrint = program[arg]
            elif mode == 1:
                print(f"Outputting immediate value {arg}.")
                toPrint = arg
            print(f'Output at PC={PC}: {toPrint}')
            PC += 2

        elif inst == 5:
            print("JNZ")
            args = program[PC+1:PC+3]
            opcodeModes = getOpcodeModes(2, fullInst)
            jumpTarget = -1337
            if opcodeModes[1] == 0:
                jumpTarget = program[args[1]]
            elif opcodeModes[1] == 1:
                jumpTarget = args[1]

            if opcodeModes[0] == 0:
                if program[args[0]] != 0:
                    print(
                        f"Value at address {args[0]} was {program[args[0]]}, not 0. Jumping to {jumpTarget}.")
                    PC = jumpTarget
                    continue
                else:
                    print(f"Value at address {args[0]} was 0. Not jumping.")

            elif opcodeModes[0] == 1:
                if args[0] != 0:
                    print(
                        f"Immediate value {args[0]} is not 0. Jumping to {jumpTarget}.")
                    PC = jumpTarget
                    continue
                else:
                    print(f"Value at address {args[0]} was 0. Not jumping.")

            PC += 3

        elif inst == 6:
            print("JIZ")
            arg = program[PC+1:PC+3]
            opcodeModes = getOpcodeModes(2, fullInst)
            jumpTarget = -1337
            if opcodeModes[1] == 0:
                jumpTarget = program[arg[1]]
            elif opcodeModes[1] == 1:
                jumpTarget = arg[1]

            if opcodeModes[0] == 0:
                if program[arg[0]] == 0:
                    print(
                        f"Value at address {arg[0]} was 0. Jumping to {jumpTarget}.")
                    PC = jumpTarget
                    continue
                else:
                    print(
                        f"Value at address {arg[0]} was {program[arg[0]]}, not 0. Not jumping.")
            elif opcodeModes[0] == 1:
                if arg[0] == 0:
                    print(
                        f"Immediate value {arg[0]} was 0. Jumping to {jumpTarget}.")
                    PC = jumpTarget
                    continue
                else:
                    print(f"Value at address {arg[0]} was not 0. Not jumping.")

            PC += 3

        elif inst == 7:
            print("LTH")
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            print(f"opcodeModes={opcodeModes}, arguments={args}")

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                print(f"Got 1st value {val1} from address {args[0]}")
            elif opcodeModes[0] == 1:
                val1 = args[0]

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                print(f"Got 2nd value {val2} from address {args[1]}")
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                print(f'This should never happen! PC={PC}')
                break

            program[dest] = 1 if val1 < val2 else 0
            PC += 4

        elif inst == 8:
            print("EQU")
            val1 = -1337
            val2 = -1337
            dest = -1
            args = program[PC+1:PC+4]
            opcodeModes = getOpcodeModes(3, fullInst)
            print(f"opcodeModes={opcodeModes}, arguments={args}")

            if opcodeModes[0] == 0:
                val1 = program[args[0]]
                print(f"Got 1st value {val1} from address {args[0]}")
            elif opcodeModes[0] == 1:
                val1 = args[0]

            if opcodeModes[1] == 0:
                val2 = program[args[1]]
                print(f"Got 2nd value {val2} from address {args[1]}")
            elif opcodeModes[1] == 1:
                val2 = args[1]

            if opcodeModes[2] == 0:
                dest = args[2]
            elif opcodeModes[2] == 1:
                print(f'This should never happen! PC={PC}')
                break

            program[dest] = 1 if val1 == val2 else 0
            PC += 4

        elif inst == 99:
            print(f'Program halted when PC={PC}')
            break

        else:
            print(f"Trying to do an illegal operation: {inst} at PC={PC}.")
            break


evalProgram(initialData)
