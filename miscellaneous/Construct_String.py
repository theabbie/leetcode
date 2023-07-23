t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = []
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
            ctr += 1
        if ctr % 2 == 1:
            res.append(s[i] * (ctr % 2))
        else:
            res.append(s[i] * 2)
        i += 1
    print("".join(res))