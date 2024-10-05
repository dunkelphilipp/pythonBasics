from os import close


def main():
    file = open('text.txt', 'r')
    text = file.read()
    all_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for element in text:
        if element in all_punct:
            text = text.replace(element, '')

    words = text.split()
    words = [word.lower() for word in words]
    unique_words = set(words)

    unique_words = sorted(unique_words)
    for word in unique_words:
        print(word)

    file.close()

main()