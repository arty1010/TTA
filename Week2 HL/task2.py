def deprecate_value(bikeValue):
    bikeValue = 0.9*bikeValue
    return bikeValue

bikeVal = 2000
count = 0
while (bikeVal >= 1000):
    count += 1
    print("In Year " + str(count) + " Bike Value will be: " + str(bikeVal))
    bikeVal = deprecate_value(bikeVal)