from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ctrs = Counter(s)
        ctrtarget = Counter(target)
        mcopy = float('inf')
        for c in ctrtarget:
            mcopy = min(mcopy, ctrs[c] // ctrtarget[c])
        return mcopy