import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(w):
            return w.count(min(w))
        n = len(words)
        words = sorted([f(w) for w in words])
        res = []
        for q in queries:
            q = f(q)
            res.append(n - bisect.bisect_right(words, q))
        return res