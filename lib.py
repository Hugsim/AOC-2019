from typing import Any, Callable, Tuple


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()


def fileIntoIntArray(fileName: str) -> [int]:
    with open(fileName) as f:
        return map(toInt, f.readlines())


def toInt(x: Any) -> int:
    return int(x)


def toList(l: Any) -> [Any]:
    return list(l)


def toStr(x: Any) -> str:
    return str(x)


def mapList(f: Callable[[Any], Any], l: [Any]) -> [Any]:
    return list(map(f, l))


maplist = mapList
listmap = mapList
listMap = mapList


def pr(x: Any) -> Any:
    print(x)
    return x


def fst(p: Tuple[Any, Any]) -> Any:
    return p[0]


def snd(p: Tuple[Any, Any]) -> Any:
    return p[1]


def nthDigitOfInt(n: int, num: int) -> int:
    return int(str(num)[n])


def sliceDigitsOfInt(start: int, end: int, num: int) -> int:
    return int(str(num)[start:end])
