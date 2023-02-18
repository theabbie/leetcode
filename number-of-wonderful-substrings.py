from collections import Counter

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ctr = Counter()
        charctr = [0] * 10
        ctr[tuple(charctr)] = 1
        for c in word:
            charctr[ord(c) - ord('a')] += 1
            ctr[tuple([p % 2 for p in charctr])] += 1
        res = 0
        for p in ctr:
            res += ctr[p] * (ctr[p] - 1) // 2
            temp = list(p)
            for x in range(10):
                if p[x] == 0:
                    temp[x] = 1
                    res += ctr[p] * ctr[tuple(temp)]
                    temp[x] = 0
        return res