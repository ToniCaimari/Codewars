import string


def high(x):
    print(x)
    albz = string.ascii_lowercase
    value_list = list(range(1, 27))
    word_list = x.split()
    guide = dict(zip(albz, value_list))
    sum_list = []
    sum = 0
    for i in word_list:
        for key, value in guide.items():
            for c in i:
                if c == key:
                    sum += value
                    continue
        sum_list.append(sum)
        sum -= sum
    Real_word_value = dict(zip(word_list, sum_list))
    Ord_word_value = dict(sorted(Real_word_value.items(), key=lambda x: x[1]))
    keys = list(Ord_word_value.keys())[::-1]
    values = list(Ord_word_value.values())[::-1]
    alert_keys = []
    for i in values:
        if len(alert_keys) == 0:
            alert_keys.append(i)
        else:
            if i == alert_keys[0]:
                alert_keys.append(i)
            else:
                break
    pre_resp = []
    for i in keys:
        if len(pre_resp) != len(alert_keys):
            pre_resp.append(i)
            continue
    return pre_resp.pop()
