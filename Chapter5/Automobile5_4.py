loan = float(input("Enter your monthly loan: "))
insurance = float(input("Enter your monthly insurance: "))
gas = float(input("Enter your monthly gas: "))
oil = float(input("Enter your monthly oil: "))
tires = float(input("Enter your monthly tires: "))
maintenance = float(input("Enter your monthly maintenance: "))

def monthlyCosts(loan, insurance, gas, oil, tires, maintenance):
    monthly = loan + insurance + gas + oil + tires + maintenance
    return monthly

def yearlyCosts(loan, insurance, gas, oil,tires, maintenance):
    yearly = (loan + insurance + gas + oil + tires + maintenance) * 12
    return yearly

print(monthlyCosts(loan, insurance, gas, oil, tires, maintenance))
print(yearlyCosts(loan, insurance, gas, oil, tires, maintenance))