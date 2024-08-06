class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        extra = 0
        ctr = Counter(s)
        for c in ctr:
            res += ctr[c] - ctr[c] % 2
            if ctr[c] & 1:
                extra = 1
        res += extra
        return res