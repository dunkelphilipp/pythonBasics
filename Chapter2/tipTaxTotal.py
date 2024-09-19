price = 10
tip = 0.18
tax = 0.07
amountMeals = input("Enter total amount of meals: ")
amountMeals = int(amountMeals)

totalAmount = amountMeals * price
totalTax = totalAmount * tax
totalTip =totalAmount * tip

print(totalTax, totalTip, totalAmount)
