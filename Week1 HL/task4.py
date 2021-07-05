bikeValue = 2000
count = 0
while (bikeValue >= 1000):
    count += 1
    print("In Year " + str(count) + " Bike Value will be: " + str(bikeValue))
    bikeValue = bikeValue - (10/100*bikeValue)
