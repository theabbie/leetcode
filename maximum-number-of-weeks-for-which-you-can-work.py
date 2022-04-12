class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = 0
        maxval = float('-inf')
        for m in milestones:
            total += m
            maxval = max(maxval, m)
        total -= maxval
        return min(2 * total + 1, total + maxval)