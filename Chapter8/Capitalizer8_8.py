def main():
    text = input("Enter a string: ")
    new_text = cap_text(text)
    for sentence in new_text:
        print(sentence, end=". ")


def cap_text(text):
    new_sentence_list = []
    sentence_list = text.split('.')
    sentence_list = sentence_list[:-1]
    for sentence in sentence_list:
        new_sentence = sentence.strip().capitalize()
        new_sentence_list.append(new_sentence)
    return new_sentence_list

if __name__ == "__main__":
    main()