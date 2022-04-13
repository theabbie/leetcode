class Solution:
    def isPalindrome(self, s, i, j):
        if i >= j - 1:
            return s[i] == s[j - 1]
        if s[i] == s[j - 1]:
            return self.isPalindrome(s, i + 1, j - 1)
        return False
    
    def getPos(self, s, i, n):
        if i == n:
            return [[]]
        op = []
        for j in range(i + 1, n + 1):
            if self.isPalindrome(s, i, j):
                curr = s[i:j]
                val = self.getPos(s, j, n)
                op += [[curr] + v for v in val]
        return op
    
    def partition(self, s: str) -> List[List[str]]:
        return self.getPos(s, 0, len(s))