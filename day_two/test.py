def mystery(word):
    if (len(word) == 0):
        return word
    else:
        return (word[1:len(word)] + mystery(word[:1]))

print(mystery("hello"))