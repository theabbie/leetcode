class Solution:
    def possible(self, nums, k, p):
        n = len(nums)
        prev = float('-inf')
        pairs = 0
        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] <= k and prev < i - 1:
                prev = i
                pairs += 1
        return pairs >= p
    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        res = float('inf')
        beg = 0
        end = nums[-1] - nums[0]
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(nums, mid, p):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res