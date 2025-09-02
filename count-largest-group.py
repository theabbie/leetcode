M = 10000
res = [0] * (M + 1)
s = [0] * (M + 1)
ctr = Counter()
mf = nm = 0

for i in range(1, M + 1):
    s[i] = s[i // 10] + i % 10
    c = ctr[s[i]] + 1
    ctr[s[i]] = c
    if c > mf:
        mf, nm = c, 1
    elif c == mf:
        nm += 1
    res[i] = nm

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return res[n]