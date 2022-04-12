def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def standard(f):
    a, b = f
    mul = gcd(a, b)
    return (a // mul, b // mul)

def add(f1, f2):
    a, b = f1
    c, d = f2
    return (a * d + b * c, b * d)

def midval(f1, f2):
    a, b = add(f1, f2)
    return (a, 2 * b)

def sec(n):
    binval = [int(b) for b in "{:b}".format(n)]
    beg = (0, 1)
    end = (1, 1)
    for b in binval:
        mid = midval(beg, end)
        if b == 0:
            end = mid
        else:
            beg = mid
    beg = standard(beg)
    end = standard(end)
    return (beg, end)

print(sec(int(input("Number? "))))
