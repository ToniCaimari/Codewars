def order(sentence):
    splt_sentence = sentence.split()
    numbers = []
    for i in sentence:
        if i.isdigit() == False:
            continue
        else:
            numbers.append(i)
    numbers_splt_dict = dict(zip(numbers, splt_sentence))
    sorted_dict = dict(sorted(numbers_splt_dict.items()))
    response = ''
    for i in sorted_dict.values():
        if len(response) != 0:
            response += ' '+i
        else:
            response += i
    return response
