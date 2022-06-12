class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        msum = 0
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        prev = {}
        i = 0
        for j in range(n):
            if nums[j] in prev:
                i = max(i, prev[nums[j]] + 1)
            msum = max(msum, p[j + 1] - p[i])
            prev[nums[j]] = j
        return msum