def chocolates_parcel(n_small, n_big, order):
    for i in range(0, n_small + 1):
        for j in range(0, n_big + 1):
            if i * 2 + j * 5 == order:
                return i
    return -1


n_small = int(input("Number of small pieces of chocolate: "))
n_big = int(input("Number of big pieces of chocolate: "))
order = int(input("Weight of parcel in grams: "))
print(chocolates_parcel(n_small, n_big, order))
