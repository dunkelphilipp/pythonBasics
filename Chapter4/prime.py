num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2 +1)):
        if (num % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")