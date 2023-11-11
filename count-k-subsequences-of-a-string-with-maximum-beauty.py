from collections import Counter

M = 10 ** 9 + 7

class Solution:
    def count(self, vals, i, rem, remctr):
        if i >= len(vals):
            return 1 if rem == 0 and remctr == 0 else 0
        key = (i, rem, remctr)
        if key in self.cache:
            return self.cache[key]
        res = 0
        if remctr > 0:
            prev = self.count(vals, i + 1, rem - vals[i], remctr - 1)
            res += vals[i] * prev
        res += self.count(vals, i + 1, rem, remctr)
        res %= M
        self.cache[key] = res
        return res
    
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        ctr = Counter(s)
        vals = sorted(ctr.values(), reverse = True)
        if len(vals) < k:
            return 0
        s = sum(vals[:k])
        self.cache = {}
        return self.count(vals, 0, s, k)