t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    start = end = float('-inf')
    x = 0
    for i in range(n):
        x += a[i]
        start = max(start, x)
    x = 0
    for i in range(n - 1, -1, -1):
        x += a[i]
        end = max(end, x)
    print(max(start, end) + sum([el for el in b if el >= 0]))