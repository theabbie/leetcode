t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    arr = list(map(int, input().split()))
    arrset = set(arr)
    b = max(arr)
    for i in range(1, b + 1):
        if i not in arrset:
            s -= i
    if s < 0 or len(arrset) < len(arr):
        print("NO")
        continue
    k = b + 1
    while s > 0:
        s -= k
        k += 1
    print("YES" if s == 0 else "NO")