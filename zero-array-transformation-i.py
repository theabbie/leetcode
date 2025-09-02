class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ctr = [0] * (n + 1)
        for l, r in queries:
            ctr[l] += 1
            ctr[r + 1] -= 1
        for i in range(n):
            ctr[i + 1] += ctr[i]
        for i in range(n):
            if ctr[i] < nums[i]:
                return False
        return True