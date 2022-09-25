t = int(input())

for tt in range(1, t + 1):
    n = int(input())
    fabrics = []
    for __ in range(n):
        c, d, u = input().split()
        fabrics.append((c, int(d), int(u)))
    a = sorted(range(n), key = lambda i: (fabrics[i][0], fabrics[i][2]))
    b = sorted(range(n), key = lambda i: (fabrics[i][1], fabrics[i][2]))
    res = 0
    for i in range(n):
        if a[i] == b[i]:
            res += 1
    print(f"Case #{tt}: {res}")