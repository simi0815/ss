def clean_mul(li):
    return list(set(li))


def contains(li1, li2):
    flag = True
    for i in li2:
        if i not in li1:
            return False
    return flag


def array_dels(n_d_li, li):
    a_index = [i for i in range(len(li))]
    a_index = set(a_index)
    b_index = set(n_d_li)
    index = list(a_index - b_index)
    _res = [li[i] for i in index]
    return _res


def array_sub(li1,li2):
    _res = li1.copy()
    for i in li2:
        _res.remove(i)
    return _res

