from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        def extended_gcd(a, b):
            s, old_s = 0, 1
            r, old_r = b, a
            while r:
                q = old_r // r
                old_r, r = r, old_r - q * r
                old_s, s = s, old_s - q * s
            return old_r, old_s, (old_r - old_s * a) // b if b else 0
        def modinv(a, m):
            g, x, _ = extended_gcd(a % m, m)
            return x % m if g == 1 else None
        M = 10 ** 9 + 7
        k = max([len(w) for w in s.split()])
        facts = [0] * (k + 1)
        facts[0] = 1
        for i in range(1, k + 1):
            facts[i] = (i * facts[i - 1]) % M
        res = 1
        for w in s.split():
            n = len(w)
            ctr = Counter(w)
            res = (res * facts[n]) % M
            for c in ctr:
                res = (res * modinv(facts[ctr[c]], M)) % M
        return res