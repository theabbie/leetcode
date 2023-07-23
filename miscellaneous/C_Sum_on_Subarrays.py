t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = [1] * n
    res[0] = -k
    print(*res)