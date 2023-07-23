t = int(input())

res = []

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + (arr[i] % 2)
    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        curr = p[-1] - p[r] + p[l] + k * (r - l)
        if curr & 1:
            res.append("YES")
        else:
            res.append("NO")

print("\n".join(res))