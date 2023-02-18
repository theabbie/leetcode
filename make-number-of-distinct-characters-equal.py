from collections import Counter

class Solution:
    def numdist(self, ctr):
        res = 0
        for i in range(26):
            if ctr[chr(ord('a') + i)] > 0:
                res += 1
        return res
    
    def isItPossible(self, word1: str, word2: str) -> bool:
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)
        for i in range(26):
            for j in range(26):
                c1 = chr(ord('a') + i)
                c2 = chr(ord('a') + j)
                if ctr1[c1] > 0 and ctr2[c2] > 0:
                    ctr1[c1] -= 1
                    ctr2[c1] += 1
                    ctr2[c2] -= 1
                    ctr1[c2] += 1
                    if self.numdist(ctr1) == self.numdist(ctr2):
                        return True
                    ctr1[c1] += 1
                    ctr2[c1] -= 1
                    ctr2[c2] += 1
                    ctr1[c2] -= 1
        return False