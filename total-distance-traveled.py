class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        ctr = 0
        while mainTank > 0:
            res += 10
            mainTank -= 1
            ctr += 1
            ctr %= 5
            if ctr == 0 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        return res