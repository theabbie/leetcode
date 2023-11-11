class Solution:
    def shortestPalindrome(self, s: str) -> str:
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            if R > i:
                P[i] = min(R - i, P[2 * C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        res = 0
        for l in range(len(s) + 1):
            if P[l + 1] == l:
                res = l
        return s[res:][::-1] + s