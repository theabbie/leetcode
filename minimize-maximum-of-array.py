class Solution:
    def check(self, arr, M):
        n = len(arr)
        extra = 0
        for i in range(n):
            if arr[i] > M:
                if arr[i] - M > extra:
                    return False
                else:
                    extra -= arr[i] - M
            else:
                extra += M - arr[i]
        return True
    
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        beg = 0
        end = max(nums)
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.check(nums, mid):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res