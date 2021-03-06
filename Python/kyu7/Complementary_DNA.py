def DNA_strand(dna):
    list = ""
    for i in dna:
        if i == "A":
            list += 'T'
        if i == 'T':
            list += 'A'
        if i == 'G':
            list += 'C'
        if i == 'C':
            list += 'G'
    return list
