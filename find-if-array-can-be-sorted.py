class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = float('-inf')
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i].bit_count() == nums[i + 1].bit_count():
                i += 1
                ctr += 1
            curr = nums[i - ctr + 1 : i + 1]
            if min(curr) < prev:
                return False
            prev = max(curr)
            i += 1
        return True