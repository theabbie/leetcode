n, m, p = map(int, input().split())

arr = [0] * n

freq = [0] * (n + 1)

for _ in range(m):
    l, r, k = map(int, input().split())
    freq[l - 1] += 1
    freq[r] -= 1

for i in range(1, n + 1):
    freq[i] += freq[i - 1]

print(freq)