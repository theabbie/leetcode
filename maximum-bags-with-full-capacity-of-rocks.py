class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diff = [capacity[i] - rocks[i] for i in range(n)]
        diff.sort()
        i = 0
        while additionalRocks > 0 and i < n:
            additionalRocks -= diff[i]
            i += 1
        if additionalRocks < 0:
            return i - 1
        return i