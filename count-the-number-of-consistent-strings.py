class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ctr = 0
        for w in words:
            if set(w).issubset(allowed):
                ctr += 1
        return ctr