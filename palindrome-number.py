class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = x
        nx = 0
        while x > 0:
            nx = 10 * nx + x % 10
            x = x // 10
        return xx == nx