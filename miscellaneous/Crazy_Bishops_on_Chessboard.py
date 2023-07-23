t = int(input())

for _ in range(t):
    n = int(input())
    odd = (n + 1) // 2
    even = n - odd
    odd -= 1
    res = min(even, odd) * 3
    res += max(odd, even) - min(odd, even)
    if n >= 2:
        res -= 1
    print(res)