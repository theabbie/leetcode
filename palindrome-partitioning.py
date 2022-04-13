class Solution:
    def getPos(self, s, i, n):
        if i == n:
            return [[]]
        if i == n - 1:
            return [[s[i]]]
        op = []
        for j in range(i + 1, n + 1):
            curr = s[i:j]
            if curr == curr[::-1]:
                val = self.getPos(s, j, n)
                op += [[curr] + v for v in val]
        return op
    
    def partition(self, s: str) -> List[List[str]]:
        return self.getPos(s, 0, len(s))