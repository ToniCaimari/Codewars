def friend(x):
    Friend_list = []
    for i in x:
        if len(i) == 4:
            Friend_list.append(i)
    return Friend_list
