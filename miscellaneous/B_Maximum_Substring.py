t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    i = 0
    res = s.count("0") * s.count("1")
    while i < n:
        ctr = 1
        while i < n - 1 and s[i] == s[i + 1]:
            ctr += 1
            i += 1
        i += 1
        res = max(res, ctr * ctr)
    print(res)