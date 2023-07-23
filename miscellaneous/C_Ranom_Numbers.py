from collections import Counter, defaultdict

t = int(input())

mp = {"A": 1, "B": 10, "C": 100, "D": 1000, "E": 10000}

def score(s):
    mxyet = ""
    res = 0
    for i in range(n - 1, -1, -1):
        curr = mp[s[i]]
        if s[i] < mxyet:
            curr = -curr
        res += curr
        mxyet = max(mxyet, s[i])
    return res

for _ in range(t):
    s = list(input())
    n = len(s)
    pos = defaultdict(lambda: [-1, -1])
    for i in range(n):
        if pos[s[i]][0] == -1:
            pos[s[i]][0] = i
        pos[s[i]][1] = i
    res = score(s)
    chars = set(s)
    for a in chars:
        for x in pos[a]:
            if x != -1:
                for c in "ABCDE":
                    s[x] = c
                    res = max(res, score(s))
                s[x] = a
    print(res)