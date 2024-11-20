def function_one(filename):
    file_data = open(filename, "r+")
    for line in file_data:
        linewords = line.split()
        for word in linewords:
            word = word.strip().strip(string.punctuation).lower()
            if word != "":
                words.append(word)
