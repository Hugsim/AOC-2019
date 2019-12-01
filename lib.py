import typing


def fileIntoArray(fileName: str) -> [str]:
    with open(fileName) as f:
        return f.readlines()
