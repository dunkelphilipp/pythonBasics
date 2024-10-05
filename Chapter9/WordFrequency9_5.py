def main():
    input_file = open('sample.txt', 'r')

    d = dict()
    for line in input_file:
        line = line.strip().lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    #for key in list(d.keys()):
    #    print(key, d[key])


    output_file = open('wordfrequency.txt', 'w')
    for key in list(d.keys()):
        output_file.write(key + " " + str(d[key]) + "\n")

    input_file.close()
    output_file.close()


main()