class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        i = j = k = None
        if n & 1:
            res.append(nums[n // 2])
            i = n // 2 - 1
            j = n // 2 + 1
            k = (n - 1) // 2
        else:
            i = n // 2 - 1
            j = n // 2
            k = n // 2
        for l in range(k):
            res.append(nums[i - l])
            res.append(nums[j + l])
        return res