t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    res = n * (n + 1) // 2
    res -= sum(map(int, input().split()))
    print(res)