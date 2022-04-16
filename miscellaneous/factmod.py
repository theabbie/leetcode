def factmod(n):
    fact = 1
    for i in range(2, n + 1):
        fact = (fact * i) % (n * n)
    return fact

print([i for i in range(1, 1001) if factmod(i) != 0])
