t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print(*([1] * n))
    elif n == 2:
        print(*[1, 3])
    else:
        x = (n - 2) * 3
        p = 0
        while p < 32 and not x & (1 << p):
            p += 1
        print(*([3 * n - 3] * (n - 2)), *[1 << p, x - (1 << p)])