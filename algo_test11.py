def globalv1():
    global res
    res = 20
    globalv2()
    globalv2()
    return res


def globalv2():
    global res
    res = res - 10

print globalv1()

print "1+1i".split('+')
