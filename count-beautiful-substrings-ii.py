from collections import Counter

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        v = [0] * (n + 1)
        c = [0] * (n + 1)
        for i in range(n):
            v[i + 1] = v[i] + int(s[i] in "aeiou")
            c[i + 1] = c[i] + int(s[i] not in "aeiou")
        res = 0
        l = 0
        for l in range(k):
            if (l * l) % k != 0:
                continue
            ctr = defaultdict(lambda: defaultdict(int))
            for j in range(n + 1):
                res += ctr[v[j] - c[j]][((k + (v[j] - l) % k) % k, (k + (c[j] - l) % k) % k)]
                ctr[v[j] - c[j]][(v[j] % k, c[j] % k)] += 1
        return res