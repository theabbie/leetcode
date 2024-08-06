class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        o = 0
        for i in range(n):
            if s[i] == '1':
                if i > 0 and s[i - 1] == '0':
                    res += o
                o += 1
        if s[-1] == '0':
            res += o
        return res