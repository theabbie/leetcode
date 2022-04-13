from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ws = Counter(s1.split()) + Counter(s2.split())
        op = []
        for w in ws:
            if ws[w] == 1:
                op.append(w)
        return op