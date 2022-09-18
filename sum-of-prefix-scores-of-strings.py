from collections import defaultdict

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ctr = defaultdict(int)
        for w in words:
            n = len(w)
            for i in range(1, n + 1):
                ctr[w[:i]] += 1
        res = []
        for w in words:
            n = len(w)
            curr = 0
            for i in range(1, n + 1):
                curr += ctr[w[:i]]
            res.append(curr)
        return res