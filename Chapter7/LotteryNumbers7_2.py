import random


def main():
    num_list = [0, 0, 0, 0, 0, 0 ,0]

    for i in range(7):
        num_list[i] = random.randint(0, 9)

    for i in range(7):
        print(num_list[i], end=' ')

if __name__ == '__main__':
    main()