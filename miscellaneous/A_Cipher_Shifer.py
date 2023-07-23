t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = []
    prev = -1
    for i in range(n):
        if s[i] == prev:
            prev = -1
        elif prev == -1:
            res.append(s[i])
            prev = s[i]
    print("".join(res))