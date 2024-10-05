def main():
    text = input("Enter a string: ")
    new_text = text.lower().replace(" ", "")
    chars = {}

    for char in new_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    max_char = max(chars, key=chars.get)
    print(max_char)


if __name__ == "__main__":
    main()

