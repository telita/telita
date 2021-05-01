def int_to_str(numero):
    print(numero)
    print("-- BEFORE --")
    print(type(numero))
    print("-- AFTER --")
    numero = str(numero)
    print(type(numero))


def str_to_int(numero):
    print(numero)
    print("-- BEFORE --")
    print(type(numero))
    print("-- AFTER --")
    numero = int(numero)
    print(type(numero))


#number = input("Type a number, like string or like an integer: ")
numero = "1"
if type(numero) == int:
    int_to_str(numero)
elif type(numero) == str:
    str_to_int(numero)
