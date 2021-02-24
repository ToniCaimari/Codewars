def count(string):
    character_list = []
    character_number = []
    for i in string:
        if i not in character_list:
            character_list.append(i)
            character_number.append(string.count(i))
    return dict(zip(character_list, character_number))
