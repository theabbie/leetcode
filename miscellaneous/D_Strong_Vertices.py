t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mx = max([a[i] - b[i] for i in range(n)])
    res = [i + 1 for i in range(n) if a[i] - b[i] == mx]
    print(len(res))
    print(*res)