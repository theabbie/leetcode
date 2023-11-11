class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + nums[i]
        res = 0
        for i in range(n):
            beg = i
            end = n - 1
            curr = i - 1
            while beg <= end:
                mid = (beg + end) // 2
                if (p[mid + 1] - p[i]) * (mid - i + 1) < k:
                    curr = mid
                    beg = mid + 1
                else:
                    end = mid - 1
            res += curr - i + 1
        return res