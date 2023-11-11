n, q = map(int, input().split())

s = input()

p = [0] * (n + 1)

for i in range(n):
    p[i + 1] += p[i]
    if i < n - 1 and s[i] == s[i + 1]:
        p[i + 1] += 1

res = []

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    res.append(p[r] - p[l])

print(*res)