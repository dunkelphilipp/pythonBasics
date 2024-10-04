def main():
    digit_series = input("Enter a serial of number digits without separator: ")
    digits = [digit.strip() for digit in digit_series]

    sum = 0
    for digit in digits:
        sum += int(digit)

    print(f"Sum of all digits: {sum}")

main()