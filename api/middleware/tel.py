def strfy_add_crossing(tel):
    n_li = list(tel)
    if len(n_li) >= 11:
        n_li.insert(-4, '-')
        n_li.insert(-8, '-')
        n_li.insert(-12, '-')
    else:
        n_li.insert(-4, '-')
        n_li.insert(-8, '-')
    crossing_tel = "".join(n_li)
    return crossing_tel
def tel_to_int(tel):
    try:
        tel = int(tel)
    except Exception:
        pass
    return tel


if __name__ == '__main__':
    print(strfy_add_crossing("13219316112"))