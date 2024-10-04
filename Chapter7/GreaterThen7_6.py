def main():
    num = 5
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    greaterThen(num_list, num)

def greaterThen(num_list, num):
    for i in num_list:
        if i > num:
            print(i, end=' ')

main()