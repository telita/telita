def number_length(num):
    count = 0
    for x in str(num):
        count = count + 1
    print(count)
    return count


num = int(input("Numero: "))
number_length(num)
