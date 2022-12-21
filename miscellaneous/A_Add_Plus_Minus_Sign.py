t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ctr = s.count("1")
    p = 0
    res = []
    for i in range(n):
        if s[i] == "1":
            if i > 0:
                res.append("+" if 2 * p < ctr else "-")
            p += 1
        elif i > 0:
            res.append("+")
    print("".join(res))