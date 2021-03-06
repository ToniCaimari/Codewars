def binary_array_to_number(arr):
    sum = 0
    count = 0
    mult_list = arr[::-1]
    for i in mult_list:
        if i == 0:
            if count == 0:
                count += 1
            else:
                count *= 2
        else:
            if count == 0:
                sum += 1
                count += 1
            else:
                count *= 2
                sum += count

    return sum
