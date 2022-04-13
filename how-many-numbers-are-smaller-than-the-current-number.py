import bisect

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        order = sorted([(num, i) for i, num in enumerate(nums)])
        for i in range(n):
            pos = bisect.bisect_left(order, (order[i][0], float('-inf')))
            ans[order[i][1]] = i - max(i - pos, 0)
        return ans