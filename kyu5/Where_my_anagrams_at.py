def anagrams(word, words):
    list = []
    for i in words:
        if sorted(i) == sorted(word):
            list.append(i)
    return list
