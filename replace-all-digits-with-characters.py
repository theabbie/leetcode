class Solution:
    def shift(self, c, n):
        return chr(ord(c) + n)
    
    def replaceDigits(self, s: str) -> str:
        op = []
        n = len(s)
        for i in range(n):
            if i & 1:
                op.append(self.shift(s[i - 1], int(s[i])))
            else:
                op.append(s[i])
        return "".join(op)