def square(a):
    if a == 0:
        return 0
    if a & 1:
        return -~((square(a >> 1) << 2) + ((a >> 1) << 2))
    else:
        return square(a >> 1) << 2

def mult(a, b):
    ans = 0
    while a != 0 and b != 0:
        if a < b:
            ans += square(a)
            b -= a
        else:
            ans += square(b)
            a -= b
    return ans

print(mult(57583434937657895454287384399683457476834868758347496666666666666666666666666875757, 464367354758457284364857486457364756484793284358465839274894679843765467469544444444444444444444444385767464))
