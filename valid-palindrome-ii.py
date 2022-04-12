class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1
        if s[i] != s[j]:
            option1 = s[:i] + s[i + 1:]
            option2 = s[:j] + s[j + 1:]
            if option1 == option1[::-1]:
                return True
            if option2 == option2[::-1]:
                return True
            return False
        return True