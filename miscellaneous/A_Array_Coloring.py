t = int(input())

res = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    found = False
    for el in arr:
        if el % 2 == (s - el) % 2:
            found = True
            break
    res.append("YES" if found else "NO")

print(*res)