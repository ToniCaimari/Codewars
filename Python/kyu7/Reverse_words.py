def reverse_words(text):
    reverse = ""
    word = text.split(' ')
    for i in word:
        if len(reverse) == 0:
            reverse += i[::-1]
            continue
        if i == word[1]:
            reverse += " "+i[::-1]
        else:
            reverse += " "+i[::-1]
    return reverse
