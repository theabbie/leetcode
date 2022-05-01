from collections import Counter

class Solution:
    def isSubset(self, ctr1, ctr2):
        for c in ctr1:
            if ctr2[c] < ctr1[c]:
                return False
        return True
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        univ = Counter()
        for w in words2:
            curr = Counter(w)
            for c in curr:
                univ[c] = max(univ[c], curr[c])
        return [w for w in words1 if self.isSubset(univ, Counter(w))]