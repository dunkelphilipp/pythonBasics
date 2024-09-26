from deep_translator import GoogleTranslator

def main():
    text = str(input("Enter a text to translate, enter 'stop' to quit: "))

    while text.lower() != 'stop':
        print(translate(text))
        text = str(input("Enter a text to translate, enter 'stop' to quit: "))

    print("Bye!")

def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

main()