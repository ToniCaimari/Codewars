def find_short(s):
    short = s.split()
    bell = min(short, key=len)
    l = len(bell)
    return l
