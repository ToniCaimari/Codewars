import string


def find_missing_letter(chars):
    check = [i.lower() for i in chars]
    abc = string.ascii_lowercase

    start = abc[abc.index(check[0]):abc.index(check[0])+len(chars)+1]

    for i in start:
        if i in check:
            continue
        else:
            if chars[0].isupper() == True:
                return i.upper()
            else:
                return i


assert(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
assert(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
