class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 1:
            if n % 3 == 0:
                n = n // 3
            elif n % 3 == 1:
                n = (n - 1) // 3
            else:
                break
        return n == 1