budget = float(input("Enter your budget: "))
expense = 0.0
day = 0

for day in range(1, 5):
    daily_expense = float(input(f"Enter your daily expense for day {day}: "))
    expense += daily_expense

print(budget - expense)
