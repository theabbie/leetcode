class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        beg = 1
        end = n // 2
        while beg <= end:
            mid = (beg + end) // 2
            p = True
            for i in range(mid):
                if nums[i] >= nums[-mid+i]:
                    p = False
                    break
            if p:
                beg = mid + 1
            else:
                end = mid - 1
        return n - 2 * (beg - 1)