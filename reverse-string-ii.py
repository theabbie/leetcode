class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        for i in range(0, n, k):
            if (i // k) % 2 == 0:
                ni = i + min(k, n - i) // 2
                for j in range(i, ni):
                    nj = min(i + k, n) - j + i - 1
                    s = s[:j] + s[nj] + s[j + 1 : nj] + s[j] + s[nj + 1:]
        return s