from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wset = set(ideas)
        ctr = [0] * 676
        pos = lambda x, y: 26 * (ord(x) - ord('a')) + ord(y) - ord('a')
        res = 0
        for w in ideas:
            for cc in range(26):
                c = chr(ord('a') + cc)
                if c + w[1:] not in wset:
                    ctr[pos(w[0], c)] += 1
                    res += 2 * ctr[pos(c, w[0])]
        return res