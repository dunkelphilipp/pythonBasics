male = int(input('Enter amount of male students: '))
female = int(input('Enter amount of female students: '))

total = male + female

male_percentage = male / total * 100
female_percentage = female / total * 100

print(f'There are {male_percentage} % male students and {female_percentage} % female students.')