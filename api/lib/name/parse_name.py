def _format_name(name):
    if name:
        return name.capitalize()
    return name


def chinese_name(str):
    for _char in str:
        if _char < '\u4e00' or _char > '\u9fa5':
            return False
    if 2 <= len(str) <= 3:
        sur = str[0:1]
        name = str[1:]
        return name,sur
    if len(str) == 4:
        sur = str[0:2]
        name = str[2:4]
        return name, sur
    raise Exception("中文名字太长了，暂不支持")


def handle_name(name,format="capital"):
    name = name.strip(" ")
    if chinese_name(name):
        return chinese_name(name)
    r_list = name.split(' ')

    name_list = []
    for item in r_list:
        if item:
            name_list.append(item)
    if format == "capital":
        name_list = list(map(_format_name, name_list))
    elif format == "upper":
        name_list = list(map(lambda x:x.upper(), name_list))
    elif format == "lower":
        name_list = list(map(lambda x:x.lower(), name_list))
    else:
        raise Exception("format没有此格式")
    if not len(name_list):
        return "",""

    if len(name_list) == 1:
        return (name_list[0], "")
    else:
        return (" ".join(name_list[:-1]), name_list[-1])



def merge_name(f_n, l_n, reverse=False):
    name_list = [f_n, l_n]
    if reverse:
        name_list.reverse()
    try:
        name_list.remove("")
        name_list.remove("")
    except Exception:
        pass
    full_name = " ".join(name_list).lower().strip(" ")
    return full_name


if __name__ == '__main__':
    print(handle_name("fs dsd",format="lower"))
