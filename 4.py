from collections import defaultdict

DICTIONARY = defaultdict(list)


def addWord(word, translation):
    DICTIONARY[word].append(translation)


def removeWord(word):
    del DICTIONARY[word]


def removeTranslated(word, translation):
    if DICTIONARY[word] and translation in DICTIONARY[word]:
        DICTIONARY[word].remove(translation)


addWord("one", "один")
addWord("first", "перший")
addWord("first", "по перше")
addWord("first", "шо")
print(DICTIONARY)
removeWord("one")
removeTranslated("first", "шо")
print(DICTIONARY)
