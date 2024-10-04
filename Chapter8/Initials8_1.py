def main():
    full_name = input("Enter Full (First, middle and last) Name: ")
    names = full_name.split()
    initials = [name[0].upper() for name in names]

    for character in initials:
        print (character, end='.')

main()