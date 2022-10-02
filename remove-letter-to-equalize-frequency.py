from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)
        for i in range(n):
            ctr = Counter(word[:i] + word[i+1:])
            if len(set(ctr.values())) == 1:
                return True
        return False