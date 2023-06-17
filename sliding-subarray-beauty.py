from collections import Counter

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ctr = [0] * 101
        res = []
        for i in range(n):
            ctr[nums[i] + 50] += 1
            if i >= k:
                ctr[nums[i - k] + 50] -= 1
            if i >= k - 1:
                rem = x
                val = 0
                for j in range(50):
                    if ctr[j] > 0:
                        rem -= ctr[j]
                    if rem <= 0:
                        val = j - 50
                        break
                res.append(val)
        return res