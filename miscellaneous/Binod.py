t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    pf = [[0] for _ in range(60)]
    for i in range(n):
        for b in range(60):
            if arr[i] & (1 << b):
                pf[b].append(pf[b][-1] + 1)
            else:
                pf[b].append(pf[b][-1])
    for _ in range(q):
        res = 0
        k, l1, r1, l2, r2 = map(int, input().split())
        xctr = r1 - l1 + 1
        yctr = r2 - l2 + 1
        x = pf[k][r1] - pf[k][l1 - 1]
        y = pf[k][r2] - pf[k][l2 - 1]
        print(x * (yctr - y) + y * (xctr - x))