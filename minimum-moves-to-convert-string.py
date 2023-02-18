class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        s = list(s)
        res = 0
        for i in range(n - 2):
            if s[i] == 'X' and (i == 0 or s[i - 1] == 'O'):
                s[i] = 'O'
                s[i + 1] = 'O'
                s[i + 2] = 'O'
                res += 1
            elif i == n - 3 and (s[i + 1] != 'O' or s[i + 2] != 'O'):
                res += 1
        return res