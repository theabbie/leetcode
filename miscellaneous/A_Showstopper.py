t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == 1:
        print("Yes")
        continue
    for i in range(n):
        a[i], b[i] = min(a[i], b[i]), max(a[i], b[i])
    amax = max(a[:-1])
    bmax = max(b[:-1])
    if a[-1] < amax:
        a[-1], b[-1] = b[-1], a[-1]
    print("Yes" if a[-1] >= amax and b[-1] >= bmax else "No")