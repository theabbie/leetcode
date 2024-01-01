from collections import Counter

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        v = [0] * (n + 1)
        c = [0] * (n + 1)
        for i in range(n):
            v[i + 1] = v[i] + int(s[i] in "aeiou")
            c[i + 1] = c[i] + int(s[i] not in "aeiou")
        res = 0
        for l in range(k):
            rem = k // self.gcd(k, l)
            ctr = [defaultdict(int) for _ in range(2 * n + 1)]
            for j in range(n + 1):
                res += ctr[n + v[j] - c[j]][((k + (v[j] - l) % k) % k, (c[j] % k) % rem)]
                ctr[n + v[j] - c[j]][(v[j] % k, (c[j] % k) % rem)] += 1
        return res