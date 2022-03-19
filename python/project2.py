print("This script will convert Imperial measurements to Metric")
miles = float(input("Please enter the number of miles: "))
yards = float(input("Please enter the number of yards: "))
feet = float(input("Please enter the number of feet: "))
inches = float(input("Please enter the number of inches: "))
totalInches = (63360 * miles) + (36 * yards) + (12 * feet) + inches
totalMeters = totalInches / 39.37
totalCent = totalMeters*100
kilometers = int(totalMeters / 1000)
meters = int(totalMeters%1000)
cent = float(totalCent%100)
print("The metric length is " + str(kilometers) + " kilometers, " + str(meters) + " meters, " + str(round(cent, 1)) + " centimeters")