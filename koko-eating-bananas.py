import math

class Solution:
    def getTime(self, piles, k):
        if k == 0:
            return float('inf')
        currh = 0
        for el in piles:
            currh += math.ceil(el / k)
        return currh
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        currh = self.getTime(piles, k)
        while currh > h:
            k *= 2
            currh = self.getTime(piles, k)
        beg = k // 2
        end = k
        while beg < end:
            mid = (beg + end) // 2
            currh = self.getTime(piles, mid)
            currnexth = self.getTime(piles, mid + 1)
            if currh > h and currnexth <= h:
                return mid + 1
            if currh > h:
                beg = mid + 1
            else:
                end = mid