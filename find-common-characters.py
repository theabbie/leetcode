from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = set.intersection(*[set(w) for w in words])
        ctrs = [Counter(w) for w in words]
        ans = []
        for c in common:
            ans += [c] * min([ctr[c] for ctr in ctrs])
        return ans