number = 1
sum = 0

while number > 0:
    number = int(input("Enter a number a positive number to continue, enter a negative number to stop: "))

    if number > 0:
        sum += number

print(f'The sum is: {sum}')
