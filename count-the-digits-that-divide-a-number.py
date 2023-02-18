class Solution:
    def countDigits(self, num: int) -> int:
        numcpy = num
        ctr = 0
        while numcpy:
            d = numcpy % 10
            if num % d == 0:
                ctr += 1
            numcpy //= 10
        return ctr