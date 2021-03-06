import string


def is_pangram(s):
    albz = string.ascii_lowercase
    for i in albz:
        if i in s.lower():
            continue
        else:
            return False
    return True
