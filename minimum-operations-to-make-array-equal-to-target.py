class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        arr = [target[i] - nums[i] for i in range(n)]
        res = abs(arr[0])
        for i in range(1, len(arr)):
            res += abs(arr[i] - arr[i - 1])
        res += abs(arr[-1])
        return res // 2