def is_isogram(string):
    clean_string = string.lower()
    list = []
    for letter in clean_string:
        if letter in list:
            return False
        list.append(letter)
    return True
