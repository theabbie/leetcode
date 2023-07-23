res = []

t = int(input())

for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    if b + c >= 10:
        res.append("YES")
    else:
        res.append("NO")

print(*res)