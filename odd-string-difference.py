from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:
        vals = []
        ctr = Counter()
        for w in words:
            n = len(w)
            d = tuple([ord(w[i + 1]) - ord(w[i]) for i in range(n - 1)])
            vals.append(d)
            ctr[d] += 1
        og = None
        for d in ctr:
            if ctr[d] > 1:
                og = d
                break
        res = None
        for i in range(len(words)):
            if vals[i] != og:
                res = words[i]
        return res