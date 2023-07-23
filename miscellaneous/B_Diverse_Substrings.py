t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, list(input())))
    mdist = len(set(s))
    res = 0
    for i in range(n):
        ctr = [0] * 10
        j = i
        dist = 0
        mocc = 0
        for j in range(i, n):
            if ctr[s[j]] == 0:
                dist += 1
            ctr[s[j]] += 1
            mocc = max(mocc, ctr[s[j]])
            if mocc <= dist:
                res += 1
            elif dist == mdist:
                break
    print(res)