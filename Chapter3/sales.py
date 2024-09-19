retailPrice = 99

quantity = int(input('How many packages are sold? '))
discountRate = 0.0
discountAmount = 0.0
fullPrice = 0.0
totalAmount = 0.0

if quantity >= 10:
    discountRate = 0.1
elif quantity <= 49:
    discountRate = 0.2
elif quantity <= 99:
    discountRate = 0.3
elif quantity <= 100:
    discountRate = 0.4
else:
    discountRate = 0

fullPrice = retailPrice * quantity
discountAmount = fullPrice * discountRate
totalAmount = fullPrice - discountAmount

print(f'Your Full Price is {fullPrice:2f}, your discount amount is {discountAmount:.2f}, your total amount is {totalAmount:.2f}')