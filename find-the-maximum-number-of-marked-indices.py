class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        beg = 1
        end = n // 2
        while beg <= end:
            mid = (beg + end) // 2
            v = True
            for i in range(mid):
                if 2 * nums[i] > nums[-mid + i]:
                    v = False
                    break
            if v:
                beg = mid + 1
            else:
                end = mid - 1
        return 2 * (beg - 1)