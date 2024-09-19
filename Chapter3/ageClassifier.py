age = int(input("Enter your age: "))

if age <= 1:
    print('infant')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age >= 20:
    print('adult')
