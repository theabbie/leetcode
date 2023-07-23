from collections import Counter

M1 = 10 ** 9 + 7
M2 = 10 ** 9 + 33
p1 = 10 ** 9 + 9
p2 = 10 ** 9 + 87
pw1 = [1] * 26
pw2 = [1] * 26
for i in range(1, 26):
    pw1[i] = p1 * pw1[i - 1]
    pw2[i] = p2 * pw2[i - 1]
    pw1[i] %= M1
    pw2[i] %= M2

class Solution:
    def mins(self, stickers, i, n, rem, rctr, h1, h2):
        if rctr == 0:
            return 0
        if i >= n:
            return float('inf')
        key = (i, h1, h2)
        if key in self.cache:
            return self.cache[key]
        a = self.mins(stickers, i + 1, n, rem, rctr, h1, h2)
        newrem = Counter(rem)
        done = True
        for c in stickers[i]:
            if newrem[c] > 0:
                done = False
                h1 = (h1 + M1 - pw1[ord(c) - ord('a')]) % M1
                h2 = (h2 + M2 - pw2[ord(c) - ord('a')]) % M2
                newrem[c] -= 1
                rctr -= 1
        b = 1 + self.mins(stickers, i + int(done), n, newrem, rctr, h1, h2)
        res = min(a, b)
        self.cache[key] = res
        return res
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        chars = set(target)
        self.cache = {}
        stickers = [s for s in stickers if len(set.intersection(set(s), chars)) > 0]
        res = self.mins(stickers, 0, len(stickers), Counter(target), len(target), 0, 0)
        if res == float('inf'):
            return -1
        return res