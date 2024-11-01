class Solution:
    def makePalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        ops = 0
        while i < j:
            if s[i] != s[j]:
                ops += 1
            i += 1
            j -= 1
        return ops <= 2