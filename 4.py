from lib import *
import typing


def isSixDigits(password: str) -> bool:
    return 99_999 < int(password) < 1_000_000


def isInRange(password: str) -> bool:
    return 245318 <= int(password) <= 765747


def hasTwoAdjacentDigitsSame(password: str) -> bool:
    result = []
    for i in range(1, len(password)):
        if (password[i - 1] == password[i]):
            result.append(i)
            return True

    # for i in result:
    #     try:
    #         if password[i] != password[i+2]:
    #             return True
    #     except e:
    #         print(password, i)
    #     # except IndexError:
    #         # return True
    return False


def hasIncreasingNumbers(password: str) -> bool:
    for i in range(len(password) - 1):
        if int(password[i]) > int(password[i+1]):
            return False
    return True


def isValidPassword(password: str) -> bool:
    return isSixDigits(password) & isInRange(password) & hasTwoAdjacentDigitsSame(password) & hasIncreasingNumbers(password)


count: int = 0
for i in range(245318, 765747 + 1):
    if isValidPassword(str(i)):
        count += 1

print(count)
