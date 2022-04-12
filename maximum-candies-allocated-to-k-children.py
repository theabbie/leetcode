class Solution:
    def numChild(self, candies, candy):
        k = 0
        for pile in candies:
            k += int(pile / candy)
        return k
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        beg = 1
        end = max(candies)
        while beg <= end:
            mid = (beg + end) // 2
            val = self.numChild(candies, mid)
            nextval = self.numChild(candies, mid + 1)
            if val >= k and nextval < k:
                return mid
            elif beg == end:
                break
            elif val < k:
                end = mid
            else:
                beg = mid + 1
        return 0