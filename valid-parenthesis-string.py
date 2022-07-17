class Solution:
    def isValid(self, s, i, n, ctr):
        if ctr < 0:
            return False
        if i >= n:
            return ctr == 0
        if (i, ctr) in self.cache:
            return self.cache[(i, ctr)]
        res = False
        if s[i] == '(':
            res = self.isValid(s, i + 1, n, ctr + 1)
        elif s[i] == ')':
            res = self.isValid(s, i + 1, n, ctr - 1)
        else:
            for diff in [-1, 0, 1]:
                if self.isValid(s, i + 1, n, ctr + diff):
                    res = True
                    break
        self.cache[(i, ctr)] = res
        return res
    
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        self.cache = {}
        return self.isValid(s, 0, n, 0)