day = int(input("Enter a day (from 1 to 31): "))
month = int(input("Enter a month (from 1 to 12): "))
year = int(input("Enter a year (from 0 to 99): "))

if day < 1 or day > 31:
    print('invalid day')
elif month < 1 or month > 12:
    print('invalid month')
elif year < 0 or year > 99:
    print('invalid year')

else:
    if (month * day) == year:
        print('This is a magic date')
    else:
        print('This is not a magic date')