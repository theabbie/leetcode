t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for el in b:
        i = a.index(min(a))
        a[i] = el
    print(sum(a))