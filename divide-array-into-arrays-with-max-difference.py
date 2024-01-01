class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = [[] for _ in range(n // 3)]
        for i in range(n):
            res[i // 3].append(nums[i])
        for i in range(n // 3):
            if res[i][2] - res[i][0] > k:
                return []
        return res