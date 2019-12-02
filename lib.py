import typing


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()


def fileIntoIntArray(fileName: str) -> [int]:
    with open(fileName) as f:
        return map(lambda x: int(x), f.readlines())


def toInt(x): 
    return int(x)
