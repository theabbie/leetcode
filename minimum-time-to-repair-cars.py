import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        beg = 0
        end = max(ranks) * cars * cars
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            rem = cars
            for el in ranks:
                curr = int(math.sqrt(mid / el))
                rem -= min(rem, curr)
            if rem == 0:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res