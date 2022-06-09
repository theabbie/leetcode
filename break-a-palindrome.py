class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        isNotA = False
        minstr = ""
        for i in range(n):
            if palindrome[i] > 'a' and 2 * i + 1 != n:
                minstr = palindrome[:i] + 'a' + palindrome[i+1:]
                isNotA = True
                break
        if not isNotA:
            return palindrome[:-1] + 'b'
        return minstr