from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        return sorted(ctr.keys(), key = lambda w: (-ctr[w], w))[:k]