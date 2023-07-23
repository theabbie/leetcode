M = 10 ** 9 + 7

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    s = input()
    pos = 0
    ctr = 0
    def genall(s, i, n, x, y):
        global ctr
        global pos
        if i >= n or y - x == 1:
            print(arr[x:y])
            pos += p[y] - p[x]
            ctr += 1
            return
        if s[i] == "L":
            for j in range(x, y - 1):
                genall(s, i + 1, n, x, j + 1)
        else:
            for j in range(x, y - 1):
                genall(s, i + 1, n, j + 1, y)
    genall(s, 0, k, 0, n)
    print((pos * pow(ctr, M - 2, M)) % M)