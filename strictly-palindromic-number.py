class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            num = []
            curr = n
            while curr:
                num.append(curr % b)
                curr = curr // b
            if num != num[::-1]:
                return False
        return True