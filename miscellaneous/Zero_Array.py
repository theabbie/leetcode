t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = n
    arr = arr + arr
    n *= 2
    a = arr[:]
    b = arr[:]
    for i in range(n):
        if i & 1:
            a[i] *= -1
        else:
            b[i] *= -1
    pos = False
    asum = bsum = 0
    for i in range(n):
        asum += a[i]
        bsum += b[i]
        if i >= k:
            asum -= a[i - k]
            bsum -= b[i - k]
        if i >= k - 1:
            if asum == 0 or bsum == 0:
                pos = True
                break
    print("YES" if pos else "NO")