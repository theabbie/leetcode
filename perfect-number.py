class Solution:
    def getFactors(self, n, factors):
        for i in range(n - 1, 0, -1):
            if i not in factors and n % i == 0:
                factors.update({i})
                factors.update({n//i})
                self.getFactors(i, factors)
    
    def checkPerfectNumber(self, num: int) -> bool:
        fsum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                fsum = fsum + i + num//i
            i += 1
        return (True if fsum == num and num!=1 else False)