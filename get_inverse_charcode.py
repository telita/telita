def get_inverse_charcode(char):
    if len(char) == 1:
        if char.islower() is True:
            print(ord(char.upper()))
        elif char.isupper() is True:
            print(ord(char.lower()))
        else:
            print(ord(char))
    else:
        print("The length of input, must be one character.")


char = input("For what char you want inverse charcode? ")
get_inverse_charcode(char)
