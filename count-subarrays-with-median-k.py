from collections import Counter

class Solution:
    def count(self, A, K):
        ctr = Counter()
        ctr[0] = 1
        res = 0
        curr = 0
        for x in A:
            curr += x
            res += ctr[curr - K]
            ctr[curr] += 1
        return res
    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] > k:
                nums[i] = 1
            elif nums[i] < k:
                nums[i] = -1
            else:
                nums[i] = n
        return self.count(nums, n) + self.count(nums, n + 1)