from collections import Counter

s = input()

p = input()

n = len(s)
k = len(p)

if n < k:
    print(0)
    exit(0)

ctr = Counter()
pctr = Counter(p)

res = 0

for i in range(n):
    ctr[s[i]] += 1
    if i >= k:
        ctr[s[i - k]] -= 1
    if i >= k - 1:
        extra = 0
        pos = True
        for cc in range(26):
            c = chr(ord('a') + cc)
            if pctr[c] >= ctr[c]:
                extra += pctr[c] - ctr[c]
            else:
                pos = False
                break
        if pos and extra == ctr['?']:
            res += 1

print(res)