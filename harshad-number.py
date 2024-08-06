class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        curr = x
        while curr:
            s += curr % 10
            curr //= 10
        if x % s == 0:
            return s
        return -1