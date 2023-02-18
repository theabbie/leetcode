class Solution:
    def possible(self, nums, cap, k):
        n = len(nums)
        prev = False
        rem = k
        for el in nums:
            if not prev and el <= cap:
                prev = True
                rem -= 1
            else:
                prev = False
        return rem <= 0
    
    def minCapability(self, nums: List[int], k: int) -> int:
        beg = 0
        end = max(nums)
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(nums, mid, k):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res