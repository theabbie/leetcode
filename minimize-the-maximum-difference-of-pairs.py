class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        beg = 0
        end = nums[-1] - nums[0]
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            ctr = 0
            prev = -1
            for i in range(n - 1):
                if nums[i + 1] - nums[i] <= mid and i > prev:
                    ctr += 1
                    prev = i + 1
            if ctr >= p:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res