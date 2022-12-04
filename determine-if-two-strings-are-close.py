from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)
        return sorted(ctr1.keys()) == sorted(ctr2.keys()) and sorted(ctr1.values()) == sorted(ctr2.values())