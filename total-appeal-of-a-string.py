class Solution:
    def appealSum(self, s: str) -> int:
        ind = lambda c: ord(s[i]) - ord('a')
        n = len(s)
        res = 0
        last = [-1] * 26
        for i in range(n):
            res += (i - last[ind(s[i])]) * (n - i)
            last[ind(s[i])] = i
        return res