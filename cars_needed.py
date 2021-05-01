import math


def cars_needed(people):
    result = int(people) / 5
    print(math.ceil(result))


people = input("How many people is in the group? ")
cars_needed(people)
