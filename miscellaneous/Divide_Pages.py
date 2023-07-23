t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    found = False
    for el in arr:
        if not (el & 1) ^ ((total - el) & 1):
            found = True
            break
    print("YES" if found else "NO")