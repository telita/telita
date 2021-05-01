def sum2(a, b):
    numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    thenum = []
    digitsa = len(a)
    digitsb = len(b)
    if digitsa >= digitsb:
        counter = digitsa
    else:
        counter = digitsb
        digitsa = digitsa - 1
        digitsb = digitsb - 1
    while counter > 0:
        getnum = 0
        for x in numlist:
            if a[digitsa] != x:
                getnum = getnum + 1
            else:
                getnum = getnum + 1
                break
    print(getnum)


a = input("First number: ")
b = input("Second number: ")
sum2(a, b)
 