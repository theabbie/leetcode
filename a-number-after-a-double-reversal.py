class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        i = 0
        if num == 0:
            return True
        while num % 10 == 0:
            num = num // 10
            i += 1
        return i == 0