class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            res += abs(i - t.index(s[i]))
        return res