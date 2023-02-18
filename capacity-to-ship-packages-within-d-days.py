class Solution:
    def numDays(self, weights, capacity):
        curr = 0
        res = 1
        for el in weights:
            if curr + el <= capacity:
                curr += el
            else:
                curr = el
                res += 1
        return res
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        beg = max(weights)
        end = sum(weights)
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.numDays(weights, mid) <= days:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res