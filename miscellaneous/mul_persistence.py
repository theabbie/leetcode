def MultiplicativePersistence(num):
    if 0 <= num < 10:
        return 0
    p = 1
    while num:
        p *= (num % 10)
        num //= 10
    return 1 + MultiplicativePersistence(p)

print(MultiplicativePersistence(4673))