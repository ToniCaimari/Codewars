def alphabet_war(fight):
    left_count = 0
    right_count = 0
    left_side = ["s", "b", "p", "w"]
    right_side = ["z", "d", "q", "m"]
    for i in fight:
        if i in left_side:
            left_count += left_side.index(i)+1
        if i in right_side:
            right_count += right_side.index(i)+1
    if left_count > right_count:
        return "Left side wins!"
    if right_count > left_count:
        return "Right side wins!"
    else:
        return "Let's fight again!"
