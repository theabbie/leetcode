class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        numFilled = 0
        numEmpty = numBottles
        while numEmpty >= numExchange:
            numFilled = (numEmpty // numExchange)
            total += numFilled
            numEmpty = numFilled + numEmpty % numExchange
        return total