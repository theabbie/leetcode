class Solution:
    def check(self, val, x):
        return "{:b}".format(val).count("1") <= x <= val
    
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        res = -1
        x = 1
        while x < 65:
            if num1 - x * num2 > 0 and self.check(num1 - x * num2, x):
                return x
            x += 1
        return res