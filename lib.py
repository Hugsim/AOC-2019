import typing


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()


def fileIntoIntArray(fileName: str) -> [int]:
    with open(fileName) as f:
        return map(lambda x: int(x), f.readlines())


def toInt(x) -> int:
    return int(x)


def toList(l):
    return list(l)


def mapList(f, l):
    return list(map(f, l))


def pr(x):
    print(x)
    return x


def fst(p):
    return p[0]


def snd(p):
    return p[1]
