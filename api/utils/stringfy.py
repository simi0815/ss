def stringfy(o):
    if isinstance(o,list):
        return list(map(lambda x:str(x),o))
    return str(o)
