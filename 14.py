from typing import Tuple
from lib import *


def parseIngredient(ingr):
    return (int((p := ingr.split(" "))[0]), p[1])


initialData: [int] = list(
    map(
        lambda p: (maplist(parseIngredient, p[0]), parseIngredient(p[1])),
        map(
            lambda p: (p[0].split(", "), p[1]),
            map(
                lambda s: s.split(" => "),
                map(lambda s: s[:-1], fileIntoArray("data14.txt")),
            ),
        ),
    )
)
print(initialData)
