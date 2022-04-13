class Solution:
    def lcs(self, text1: str, text2: str, i, j) -> int:
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i >= len(text1) or j >= len(text2):
            self.cache[(i, j)] = 0
            return 0
        if text1[i] == text2[j]:
            self.cache[(i, j)] = 1 + self.lcs(text1, text2, i + 1, j + 1)
            return self.cache[(i, j)]
        else:
            a = self.lcs(text1, text2, i + 1, j)
            b = self.lcs(text1, text2, i, j + 1)
            self.cache[(i, j)] = max(a, b)
            return self.cache[(i, j)]
        
    def longestCommonSubsequence(self, text1: str, text2: str, i = 0, j = 0) -> int:
        self.cache = {}
        return self.lcs(text1, text2, 0, 0)