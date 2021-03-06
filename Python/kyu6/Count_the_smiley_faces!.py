def count_smileys(arr):
    valid_face_el = [':', ')', 'D', ';', '-', '~']
    count = 0
    finish = False
    smile = True
    for i in arr:
        for c in i:
            if c in valid_face_el:
                if c == ')':
                    finish = True
                    continue
                if c == ']':
                    finish = True
                    continue
                if c == 'D':
                    finish = True
                    continue
            else:
                smile = False
                break
        if smile == True:
            if finish == True:
                finish = False
                count += 1
        else:
            smile = True
    return count
