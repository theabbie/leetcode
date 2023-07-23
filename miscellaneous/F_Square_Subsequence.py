M = 998244353

def counttest(a, b):
    m = len(a)
    n = len(b)
    aset = set()
    bset = set()
    for mask in range(1, 1 << m):
        curr = []
        for i in range(m):
            if mask & (1 << i):
                curr.append(a[i])
        aset.add("".join(curr))
    for mask in range(1, 1 << n):
        curr = []
        for i in range(n):
            if mask & (1 << i):
                curr.append(b[i])
        bset.add("".join(curr))
    return len(set.intersection(aset, bset))

def count(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    lasta = [-1] * m
    lastb = [-1] * n
    pos = {}
    for i in range(m):
        if a[i] in pos:
            lasta[i] = pos[a[i]]
        pos[a[i]] = i
    pos = {}
    for i in range(n):
        if b[i] in pos:
            lastb[i] = pos[b[i]]
        pos[b[i]] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if lasta[i - 1] != -1:
                dp[i][j] -= dp[lasta[i - 1] + 1][j]
            if lastb[j - 1] != -1:
                dp[i][j] -= dp[i][lastb[j - 1] + 1]
            if lasta[i - 1] != -1 and lastb[j - 1] != -1:
                dp[i][j] += dp[lasta[i - 1] + 1][lastb[j - 1] + 1]
            dp[i][j] %= M
    return dp[m][n]

print(count("aaabbbccc", "aabbcc"), counttest("aaabbbccc", "aabbcc"))

s = input()

n = len(s)

res = 0

for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            res += count(s[:i], s[i+1:j])
            res %= M

print(res)