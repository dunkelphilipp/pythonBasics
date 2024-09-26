import random

def main():
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    question(x, y)

def question(x, y):
    answer = x + y
    tries = 3
    for i in range (tries):
        guess = int(input(f"{x} + {y} = _____"))
        if guess != answer:
            triesLeft = (tries - i) -1
            print(f"Your wrong! You have {triesLeft} tries left")
        else:
            print("Congrats! Your answer is correct.")
            break


main()