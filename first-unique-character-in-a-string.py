class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] not in s[:i] + s[i + 1:]:
                return i
        return -1