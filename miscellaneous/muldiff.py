sqmap = {}

def square(x):
    if x in sqmap:
        return sqmap[x]
    res = x * x
    sqmap[x] = res
    return res

def mul(a, b):
    res = square(a + b) - square(a - b)
    return res >> 2