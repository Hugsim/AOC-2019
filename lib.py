from typing import Any, Callable, Tuple


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()


def fileIntoIntArray(fileName: str) -> [int]:
    with open(fileName) as f:
        return map(toInt, f.readlines())


def toInt(x: Any) -> int:
    return int(x)

def toFloat(x: Any) -> float:
    return float(x)


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


def trd(p: Tuple[Any, Any, Any]) -> Any:
    return p[2]


def nthDigitOfInt(n: int, num: int) -> int:
    return int(str(num)[n])


def sliceDigitsOfInt(start: int, end: int, num: int) -> int:
    return int(str(num)[start:end])

def find(arr: [Any], elem: Any) -> int:
    for i in range(len(arr)):
        if arr[i] == elem:
            return i

def find2d(arr: [[Any]], elem: Any) -> Tuple[int, int]:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == elem:
                return (i, j)