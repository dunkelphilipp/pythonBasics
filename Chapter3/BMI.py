bmi = 0.0
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))

bmi = weight/ height ** 2

if bmi < 18.5:
    print (f'Your underweight, your BMI is {bmi:.2f}')
elif bmi > 25:
    print (f'Your overweight, your BMI is {bmi:.2f}')
else:
    print (f'Your weight is optimal, your BMI is {bmi:.2f}')
