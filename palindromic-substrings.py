class Solution:
    def countSubstrings(self, s: str, i = 0) -> int:
        n = len(s)
        if i == n - 1:
            return 1
        k = self.countSubstrings(s, i + 1)
        ctr = 0
        for j in range(i + 1, n + 1):
            if s[i:j] == s[i:j][::-1]:
                ctr += 1
        return ctr + k