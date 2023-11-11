class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        char = [0] * 26
        res = 0
        longest = 0
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            if i > 0 and (ord(s[i - 1]) - ord('a') + 1) % 26 == curr:
                longest += 1
            else:
                longest = 1
            char[curr] = max(char[curr], longest)
        return sum(char)