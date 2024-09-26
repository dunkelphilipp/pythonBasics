def main():
    sum = 0
    content = ""
    
    try:
        file = open("numbers.txt", "r")
        for line in file:
            content = int(line)
            sum += content
    except Exception:
        print("File not found")

    print(sum)

main()