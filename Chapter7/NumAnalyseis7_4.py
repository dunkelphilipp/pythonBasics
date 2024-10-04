def main():
    num_list = []

    for i in range (20):
        number = int(input("Enter a number: "))
        num_list.append(number)

    max_num = max(num_list)
    min_num = min(num_list)
    total = sum(num_list)
    average = total / len(num_list)

    print(max_num, min_num, total, average)

if __name__ == '__main__':
    main()
