class Solution:
    def md(self, word1, word2, i1, i2):
        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]
        if i1 == len(word1):
            return len(word2) - i2
        if i2 == len(word2):
            return len(word1) - i1
        if word1[i1] == word2[i2]:
            self.cache[(i1, i2)] = min(self.md(word1, word2, i1 + 1, i2 + 1), 1 + self.md(word1, word2, i1, i2 + 1), 1 + self.md(word1, word2, i1 + 1, i2))
            return self.cache[(i1, i2)]
        else:
            self.cache[(i1, i2)] = 1 + min(self.md(word1, word2, i1, i2 + 1), self.md(word1, word2, i1 + 1, i2))
            return self.cache[(i1, i2)]
    
    def minDistance(self, word1: str, word2: str) -> int:
        self.cache = {}
        return self.md(word1, word2, 0, 0)