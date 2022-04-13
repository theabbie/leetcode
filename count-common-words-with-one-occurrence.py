from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        op = set()
        for a in w1:
            if w1[a] == 1 and w2[a] == 1:
                op.add(a)
        for a in w2:
            if w1[a] == 1 and w2[a] == 1:
                op.add(a)
        return len(op)