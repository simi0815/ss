# 数组去重
def clean_mul(li):
    return list(set(li))


# 返回li1是否包含li2
def contains(li1, li2):
    flag = True
    for i in li2:
        if i not in li1:
            return False
    return flag


# 删除掉li中下标在n_d_li中的元素
def array_dels(n_d_li, li):
    a_index = [i for i in range(len(li))]
    a_index = set(a_index)
    b_index = set(n_d_li)
    index = list(a_index - b_index)
    _res = [li[i] for i in index]
    return _res


# li1中剔除li2中的元素
def array_sub(li1, li2):
    _res = li1.copy()
    for i in li2:
        _res.remove(i)
    return _res


# 返回li1和li2有没有相同元素
def is_has_same(li1, li2):
    flag = False
    for i in li1:
        if i in li2:
            flag = True
    return flag


# 合并并去重两个数组
def merge_and_dup(li1, li2):
    res = li1.copy()
    res.extend(li2)
    return clean_mul(res)


# lis是一个二维数组，如果两行有相同数值就合并
def deal_merge_list(lis):
    _lis = lis.copy()
    while True:
        flag = False
        for i in range(len(_lis) - 1):
            for j in range(i + 1, len(_lis)):
                if is_has_same(_lis[i], _lis[j]):
                    mer_li = merge_and_dup(_lis[i],_lis[j])
                    _lis.append(mer_li)
                    _lis = array_dels([i,j],_lis)
                    flag = True
                    break
            break
        if not flag:
            break
    return _lis


