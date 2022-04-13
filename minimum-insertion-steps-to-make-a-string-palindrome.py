class Solution:
    def minIns(self, s, i, j):
        if i == j:
            return 0
        if i == j - 1:
            if s[i] == s[j]:
                return 0
            return 1
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if s[i] == s[j]:
            curr = self.minIns(s, i + 1, j - 1)
            self.cache[(i, j)] = curr
            return curr
        else:
            curr = 1 + min(self.minIns(s, i + 1, j), self.minIns(s, i, j - 1))
            self.cache[(i, j)] = curr
            return curr
        
    def minInsertions(self, s: str) -> int:
        self.cache = {}
        return self.minIns(s, 0, len(s) - 1)