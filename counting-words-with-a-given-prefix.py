class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for w in words:
            if w.startswith(pref):
                res += 1
        return res