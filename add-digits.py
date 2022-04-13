class Solution:
    def addDigits(self, num: int) -> int:
        k = num % 9
        if k == 0:
            if num == 0:
                return 0
            return 9
        else:
            return k