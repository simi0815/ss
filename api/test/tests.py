def foo():
    msg=  "hello"
    def b():
        nonlocal msg
        print(msg)
    b()
foo()


def remove_cross(tel):
    tel = str(tel)

    return tel.replace("-","")
print(remove_cross("1-316-871-3930"))
