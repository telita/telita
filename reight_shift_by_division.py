import math


def shift_to_right(x, y):
    if y >= 0:
        print(math.floor(x / (2 ** y)))
        return math.floor(x / (2 ** y))


x = int(input("X: "))
y = int(input("Y: "))
shift_to_right(x, y)
