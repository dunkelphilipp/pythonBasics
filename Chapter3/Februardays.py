febDays = 28
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    febDays = febDays + 1
    print(f'{year} is a leap year, February has {febDays} days')
elif year % 4 == 0 and year % 100 != 0:
    febDays = febDays + 1
    print(f'{year} is a leap year, February has {febDays} days')

else:
    print(f'{year} is not a leap year, February has {febDays} days')