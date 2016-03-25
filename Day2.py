mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())
totalCost = mealCost * (tipPercent/100) + mealCost * (taxPercent/100) + mealCost
round(totalCost)

print ("The total meal cost is " + str(round(totalCost)) + " dollars." )
