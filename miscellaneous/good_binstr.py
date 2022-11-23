t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    res = 0
    ctr01 = 0
    ctr10 = 0
    for i in range(n - 1):
        if s[i:i+2] == "01":
            ctr01 += 1
        elif s[i:i+2] == "10":
            ctr10 += 1
    for i in range(n):
        newctr01 = ctr01
        newctr10 = ctr10
        l = None
        r = None
        if i > 0:
            l = s[i - 1]
        if i < n - 1:
            r = s[i + 1]
        if s[i] == "0":
            if l == "0":
                newctr01 += 1
            if l == "1":
                newctr10 -= 1
            if r == "0":
                newctr10 += 1
            if r == "1":
                newctr01 -= 1
        else:
            if l == "0":
                newctr01 -= 1
            if l == "1":
                newctr10 += 1
            if r == "0":
                newctr10 -= 1
            if r == "1":
                newctr01 += 1
        if newctr01 == newctr10:
            res += 1
    print(res)