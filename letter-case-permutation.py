class Solution:
    def getStr(self, s, i, n, curr):
        if i >= n:
            self.res.append(curr)
            return
        if s[i].isdigit():
            self.getStr(s, i + 1, n, curr + s[i])
        else:
            self.getStr(s, i + 1, n, curr + s[i].lower())
            self.getStr(s, i + 1, n, curr + s[i].upper())
    
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        n = len(s)
        self.getStr(s, 0, n, "")
        return self.res