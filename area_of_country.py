def area_of_country(name, area):
    percent = "{:.2f}".format((area / 148940000) * 100)
    print("%s is %s%% of the total world's landmass" % (name, percent))
    return "%s is %s%% of the total world's landmass" % (name, percent)


name = input("Ciudad: ")
area = float(input("Area: "))
area_of_country(name, area)
