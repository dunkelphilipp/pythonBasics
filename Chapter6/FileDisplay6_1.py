def main():
    
    try:
        file = open("numbers.txt", "r")
        print(file.read())
        file.close()
    except Exception:
        print("IO Error occurred")

main()