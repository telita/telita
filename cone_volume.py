import math


def cone_volume(r, h, v):
    third = 0.33333333333
    pi = 3.14
    if not(v):
        result = third * pi * float(h) * (float(r)**2)
    elif not(r):
        result = math.sqrt((3 * float(v)) / (pi * float(h)))
    else:
        result = (3 * float(v)) / (pi * (float(r)**2))
    print(result)


print("Welcome to cone calculator. You need to specify two parameters and i will calculate the other!!")
r = input("What is the RADIUS of the cone?: ")
h = input("What is the HEIGHT of the cone?: ")
v = input("What is the VOLUME of the cone?: ")
if all((r, h, v)):
    print("Is not possible to pass all three paremeters!!")
else:
    cone_volume(r, h, v)
