from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True
        ctr = Counter(s)
        oddctr = sum(1 if v & 1 else 0 for v in ctr.values())
        if oddctr > k:
            return False
        return True