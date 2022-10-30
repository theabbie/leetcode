class Solution:
    def cost(self, nums, cost, p):
        n = len(nums)
        res = 0
        for i in range(n):
            res += abs(nums[i] - p) * cost[i]
        return res
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        beg = 1
        end = max(nums)
        res = float('inf')
        while beg < end:
            mid = (beg + end) // 2
            mid1val = self.cost(nums, cost, mid)
            mid2val = self.cost(nums, cost, mid + 1)
            if mid1val <= mid2val:
                res = min(res, mid1val)
                end = mid - 1
            else:
                res = min(res, mid2val)
                beg = mid + 1
        return res
            