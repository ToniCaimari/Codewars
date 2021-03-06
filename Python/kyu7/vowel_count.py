def get_count(input_str):
    num_vowels = []
    vow = ['a', 'e', 'i', 'o', 'u']
    for i in input_str:
        if i in vow:
            num_vowels.append(i)

    return len(num_vowels)
