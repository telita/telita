def family_relation(familiar_name):
    is_family = True
    lower_familiar_name = familiar_name.lower()

    if lower_familiar_name == "darth vader":
        relationship1 = "father"
        relationship2 = "son"
    elif lower_familiar_name == "leia":
        relationship1 = "sister"
        relationship2 = "brother"
    elif lower_familiar_name == "han":
        relationship1 = "brother in law"
        relationship2 = "brother in law"
    elif lower_familiar_name == "r2d2":
        relationship1 = "droid"
        relationship2 = "human"
    else:
        print("%s is not family of Luke" % (familiar_name.title()))
        is_family = False

    if is_family is True:
        print("The relationship between %s and Luke is %s and %s" % (familiar_name.title(), relationship1, relationship2))


familiar_name = input()
family_relation(familiar_name)
