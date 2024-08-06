from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        beg = 1
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            pos = False
            ctr = Counter()
            greater = 0
            for i in range(n):
                ctr[nums[i]] += 1
                if ctr[nums[i]] == k + 1:
                    greater += 1
                if i >= mid:
                    ctr[nums[i - mid]] -= 1
                    if ctr[nums[i - mid]] == k:
                        greater -= 1
                if i >= mid - 1 and greater == 0:
                    pos = True
                    break
            if pos:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res