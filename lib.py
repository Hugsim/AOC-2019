from typing import Any, Callable


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()


def fileIntoIntArray(fileName: str) -> [int]:
    with open(fileName) as f:
        return map(lambda x: int(x), f.readlines())


def toInt(x: Any) -> int:
    return int(x)


def toList(l: Any) -> [Any]:
    return list(l)


def mapList(f: Callable[[Any], Any], l: [Any]) -> [Any]:
    return list(map(f, l))


def pr(x: Any) -> Any:
    print(x)
    return x


def fst(p: (Any, Any)) -> Any:
    return p[0]


def snd(p: (Any, Any)) -> Any:
    return p[1]
