def wordFreq(file: str) -> int:
    poem = open(file, "r")
    poem = poem.read()

    poem.replace("-", " ")
    poem = poem.lower().split()
    

    wordCount = {}
    for word in poem:
        # Keep track of each individual word. If the word is not in the dictionary, set value to 1
        if wordCount.get(word) == None:
            wordCount[word] = 1
        # Word already exists in dict
        else:
            wordCount[word] += 1

    mostFrequentWord = ('', 0)
    for key, value in wordCount.items():
        if value > mostFrequentWord[1]:
            mostFrequentWord = (key, value)

    print(mostFrequentWord)
    return mostFrequentWord[0]

wordFreq("homework/week03_CSS_HTML_Python/sample/theRoadNotTaken.txt")