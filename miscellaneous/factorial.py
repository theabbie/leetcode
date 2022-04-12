def extraLongFactorials(n):
    twos = 0
    fives = 0
    factorial = 1
    for i in range(1, n + 1):
        curr = i
        while curr % 2 == 0:
            curr = curr // 2
            twos += 1
        while curr % 5 == 0:
            curr = curr // 5
            fives += 1
        factorial *= curr
    if twos > fives:
        for _ in range(twos - fives):
            factorial *= 2
        factorial = ("{:}" + "0" * fives).format(factorial) 
    else:
        for _ in range(fives - twos):
            factorial *= 5
        factorial = ("{:}" + "0" * twos).format(factorial)
    print(factorial)

extraLongFactorials(1000)