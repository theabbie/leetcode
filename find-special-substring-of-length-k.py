class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
                ctr += 1
            if ctr == k:
                return True
            i += 1
        return False