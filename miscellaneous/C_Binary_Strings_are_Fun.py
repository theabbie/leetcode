t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    a = [None] * (2 * n - 1)
    for i in range(n):
        a[2 * i] = s[i]
    res = 0
    ctr = [0, 0]
    spaces = 0
    for i in range(2 * n - 1):
        if a[i] == None:
            spaces += 1
        else:
            ctr[int(a[i])] += 1
            if a[i] == '0':
                res += 0
    print(res % 998244353)