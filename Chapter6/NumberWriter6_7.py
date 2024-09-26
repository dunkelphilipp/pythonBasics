def main():
    amount = int(input("Enter amount of numbers to write: "))


    file = open("write.txt", "w")
    for i in range(amount):
        num = int(input("Enter a number: "))
        file.write(str(num) + "\n")

    file = open("write.txt", "r")
    print(file.read())
    file.close()

if __name__ == "__main__":
    main()
