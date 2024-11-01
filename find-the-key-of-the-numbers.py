class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        pw = 1
        for _ in range(4):
            curr = min(num1 % 10, num2 % 10, num3 % 10)
            res += pw * curr
            num1 //= 10
            num2 //= 10
            num3 //= 10
            pw *= 10
        return res