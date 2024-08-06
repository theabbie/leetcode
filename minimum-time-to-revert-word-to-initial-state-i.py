class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        dels = 1
        while dels * k < n:
            suff = n - dels * k
            if word[:suff] == word[-suff:]:
                return dels
            dels += 1
        return dels