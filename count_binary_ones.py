def count_binary_ones(decimal):
    binary = []
    while int(decimal) > 0:
        if (int(decimal) % 2) == 0:
            binary.insert(0, 0)
        else:
            binary.insert(0, 1)
        decimal = int(decimal) / 2
    print("".join(map(str, binary)))
    print(binary.count(1))


decimal = input("Insert a decimal number: ")
count_binary_ones(decimal)
