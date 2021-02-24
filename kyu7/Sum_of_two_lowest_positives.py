def sum_two_smallest_numbers(numbers):
    Snumbers = sorted(numbers)
    list = []

    for n in Snumbers:
        if n >= 0:
            list.append(n)
        else:
            continue
    su_list = list[0:2]
    return sum(su_list)
