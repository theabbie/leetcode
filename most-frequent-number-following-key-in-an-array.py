class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        ctr = {}
        for i in range(n):
            if nums[i] == key:
                if i < n - 1:
                    ctr[nums[i + 1]] = ctr.get(nums[i + 1], 0) + 1
        return max((v, k) for k, v in ctr.items())[1]