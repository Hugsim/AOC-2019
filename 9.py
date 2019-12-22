import typing
from lib import *
from intcode import evalProgram

initialData: [int] = mapList(toInt, fileIntoArray("data9.txt")[0].split(","))

output = evalProgram(initialData, [2])

print(output)
