def divofdiv(n):
    for i in range(1, n + 1):
        if n % i == 0:
            k = n // i
            print(i, k)
    
print(divofdiv(4))
print(divofdiv(5))