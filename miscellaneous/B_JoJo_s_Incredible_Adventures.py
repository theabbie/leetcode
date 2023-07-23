t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    if s == "1" * n:
        print(n * n)
        continue
    s = s + s
    n = len(s)
    res = 0
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
            ctr += 1
        if s[i] == '1':
            res = max(res, ((ctr + 1) * (ctr + 1)) // 4)
        i += 1
    print(res)