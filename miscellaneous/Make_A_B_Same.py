t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    oneseen = False
    for i in range(n):
        if a[i] == 0:
            if b[i] == 1 and 0 < i < n - 1 and oneseen:
                a[i] = 1
        else:
            oneseen = True
    oneseen = False
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            if b[i] == 1 and 0 < i < n - 1 and oneseen:
                a[i] = 1
        else:
            oneseen = True
    print("YES" if a == b else "NO")