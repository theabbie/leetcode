t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    for __ in range(n):
        a, b = map(int, input().split())
        if b < a:
            res += 1
    print(res)