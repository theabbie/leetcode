class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float('inf')] * n
        lastpos = float('-inf')
        for i in range(n):
            if s[i] == c:
                lastpos = i
            res[i] = min(res[i], i - lastpos)
        lastpos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                lastpos = i
            res[i] = min(res[i], lastpos - i)
        return res