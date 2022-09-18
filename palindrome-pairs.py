class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        pos = {}
        for i in range(n):
            pos[words[i]] = i
        res = set()
        for i, w in enumerate(words):
            m = len(w)
            for j in range(m + 1):
                currbeg = w[:j][::-1]
                currend = w[m - j:][::-1]
                pbeg = w + currbeg
                pend = currend + w
                if pbeg == pbeg[::-1] and currbeg in pos and i != pos[currbeg]:
                    res.add((i, pos[currbeg]))
                if pend == pend[::-1] and currend in pos and i != pos[currend]:
                    res.add((pos[currend], i))
        return list(res)