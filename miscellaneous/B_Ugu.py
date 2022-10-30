t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print(0)
        continue
    res = 0
    vals = []
    i = 0
    while i < n:
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        vals.append(s[i])
        i += 1
    s = "".join(vals)
    n = len(s)
    o = 0
    for i in range(n):
        if s[i] == "1":
            o += 1
        if (s[i] == "0" and o % 2 == 0) or (s[i] == "1" and o % 2 == 1):