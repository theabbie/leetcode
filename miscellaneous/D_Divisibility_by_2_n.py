t = int(input())

def numtwos(n):
    twos = 0
    while n % 2 == 0:
        twos += 1
        n = n // 2
    return twos

def genarr(n):
    res = []
    for i in range(17, 0, -1):
        l = (n // (1 << i) - 1) // 2
        if l >= 0:
            res.extend([i] * (l + 1))
    return res + [0] * max(n - len(res), 0)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = 1 << n
    twos = 0
    for el in arr:
        twos += numtwos(el)
    if twos >= n:
        print(0)
    else:
        diff = n - twos
        twos = genarr(n)
        i = 0
        while diff > 0 and i < n:
            diff -= twos[i]
            i += 1
        print(i if i < n else -1)