class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        diff = [capacity[i] - rocks[i] for i in range(n)]
        diff.sort(reverse = True)
        while len(diff) > 0 and diff[-1] <= additionalRocks:
            additionalRocks -= diff.pop()
        return n - len(diff)