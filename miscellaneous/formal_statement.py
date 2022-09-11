t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(a[0])
    pos = True
    for i in range(n):
        if a[i] > b[i] or max(a[i], a[i + 1] + 1) < b[i]:
            pos = False
            break
    if pos:
        print("YES")
    else:
        print("NO")