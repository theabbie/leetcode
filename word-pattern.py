class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patt = []
        pattset = {}
        i = 0
        for p in pattern:
            if p not in pattset:
                pattset[p] = i
                i += 1
            patt.append(pattset[p])
        words = []
        wordset = {}
        i = 0
        for w in s.split():
            if w not in wordset:
                wordset[w] = i
                i += 1
            words.append(wordset[w])
        return patt == words