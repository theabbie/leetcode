class Solution:
    def rev(self, n):
        res = 0
        while n:
            res = 10 * res + n % 10
            n //= 10
        return res
    
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num <= 18:
            return num % 2 == 0 or num % 11 == 0
        elif num < 100:
            return num % 11 == 0
        for i in range(num + 1):
            a = i
            b = num - i
            if self.rev(a) == b:
                return True
        return False