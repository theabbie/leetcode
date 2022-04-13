from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)
        for c in "abcdefghijklmnopqrstuvwxyz":
            if abs(ctr1[c] - ctr2[c]) > 3:
                return False
        return True