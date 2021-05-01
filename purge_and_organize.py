def purge_and_organize(my_list):
    result = list(set(my_list))
    result.sort()
    print(result)


r = "y"
my_list = []

while r == "y":
    my_list.append(input("Add number to the list: "))
    r = input("Add another number to the list (y/n)?: ")

purge_and_organize(my_list)
