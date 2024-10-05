def main():
    sum_words = 0
    sum_lines = 0

    file = open('text.txt', 'r')
    for line in file:
        words = line.split()
        sum_words += len(words)
        sum_lines += 1

    avg_words = sum_words / sum_lines
    print(avg_words)
    file.close()


main()