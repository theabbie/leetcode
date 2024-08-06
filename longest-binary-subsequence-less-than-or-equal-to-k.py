class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        s = s[::-1]
        n = len(s)
        zeroes = s.count('0')
        res = zeroes
        p = 0
        ones = 0
        for i in range(n):
            if s[i] == '1':
                ones += 1
                p += 1 << i
                if p > k:
                    break
                res = max(res, zeroes + ones)
        return res