t = int(input())

def count(val):
    res = 0
    while val > 2:
        res += 1
        val = val // 2
    if val == 2:
        res += 2
    if val == 1:
        res += 1
    return res

for _ in range(t):
    s = input()
    n = len(s)
    res = float('inf')
    for c in set(s):
        i = 0
        curr = 0
        while i < n:
            ctr = 1
            while i < n - 1 and not ((s[i] == c) ^ (s[i + 1] == c)):
                ctr += 1
                i += 1
            if s[i] != c:
                curr = max(curr, ctr)
            i += 1
        res = min(res, count(curr))
    print(res)