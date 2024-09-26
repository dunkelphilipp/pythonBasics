import sympy

num = int(input("Enter a number: "))

if sympy.isprime(num):
    print ("Prime")
else:
    print ("Not Prime")