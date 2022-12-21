class Solution:
    def possible(self, nums, m, k):
        n = len(nums)
        res = 0
        i = 0
        for j in range(n):
            while nums[j] - nums[i] > m:
                i += 1
            res += j - i
        return res >= k
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        beg = 0
        end = nums[-1] - nums[0]
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(nums, mid, k):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res