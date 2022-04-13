from collections import Counter

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)
        patterns = Counter(patterns)
        lens = set([len(p) for p in patterns])
        ctr = 0
        for l in lens:
            for i in range(0, n - l + 1):
                curr = word[i:i+l]
                if curr in patterns:
                    ctr += patterns[curr]
                    del patterns[curr]
        return ctr