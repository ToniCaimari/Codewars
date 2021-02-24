def first_n_smallest(arr, n):
    smallest_list = []
    lowest_ord_list = sorted(arr)[0:n]
    for i in arr:
        if i in lowest_ord_list:
            if len(smallest_list) < n:
                if smallest_list.count(i) != lowest_ord_list.count(i):
                    smallest_list.append(i)
    return smallest_list
