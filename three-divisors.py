class Solution:
    def isThree(self, n: int) -> bool:
        ctr = 0
        for i in range(1, n + 1):
            if n % i == 0:
                ctr += 1
        return ctr == 3