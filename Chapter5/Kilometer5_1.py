def main():
    kilometer = 0.0
    kilometer = float(input("Enter kilometer: "))
    showMiles(kilometer)

def showMiles (kilometer):
    miles = kilometer * 1.609
    print(f'{kilometer:.1f}km are {miles} miles')

main()