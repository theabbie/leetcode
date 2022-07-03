class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        mindels = float('inf')
        for i in range(1, n + 1):
            currdels = nums[i - 1] * (2 * i - n) - 2 * p[i]
            mindels = min(mindels, currdels)
        return mindels + p[-1]