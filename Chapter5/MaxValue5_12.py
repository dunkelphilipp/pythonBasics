def main():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    maxValue(num1, num2)

def maxValue(num1, num2):
    if num1 > num2:
        print(f"{num1} > {num2}")
    elif num2 > num1:
        print(f"{num2} > {num1}")
    else:
        print("Both number are Equal.")

main()