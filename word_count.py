#exercise 2

def word_count(file,n):
    file_object = open(file, "r")
    word = []
    for line in file_object:
        words = line.split()
        word.append(words)

    allwords = {}

    for i in range(0,len(word)):
        for j in range(0,len(word[i])):
            if word[i][j] not in allwords:
                allwords[word[i][j]] = 1
            elif word[i][j] in allwords:
                allwords[word[i][j]] += 1
    
    counts = list(allwords.values())
    counts_sorted = sorted(counts, reverse=True)
    wordlist = list(allwords.keys())

    for i in range(0,n):
        index = counts.index(counts_sorted[i])
        print(wordlist[index] + ",", counts_sorted[i])

word_count("article.txt", 10)
