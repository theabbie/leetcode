t = int(input())

for _ in range(t):
    n = int(input())
    res = list(range(n))
    xor = [0, 0]
    for i in range(n):
        xor[i % 2] ^= res[i]
    while xor[0] != xor[1]:
        xor[(n - 1) % 2] ^= res[n - 1] ^ (res[n - 1] + 1)
        xor[(n - 2) % 2] ^= res[n - 2] ^ (res[n - 2] + 1)
        res[n - 1] += 1
        res[n - 2] += 1
    print(*res)