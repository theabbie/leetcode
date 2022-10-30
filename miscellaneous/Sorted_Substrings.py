t  =int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            res += 1
    print(res)