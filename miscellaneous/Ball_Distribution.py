t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    ctr = [0] * (n + 1)
    a = list(map(int, input().split()))
    for el in a:
        ctr[0] += 1
        ctr[el] -= 1
    print(ctr)
    for i in range(1, n + 1):
        ctr[i] += ctr[i - 1]
    print(ctr)
    print(ctr.count(m))