class Solution:
    def isSubsetSum(self, arr, total, n):
        if total == 0:
            return True
        if total != 0 and n == 0:
            return False
        if (n, total) in self.cache:
            return self.cache[(n, total)]
        if 2 * arr[n - 1] > total:
            return self.isSubsetSum(arr, total, n - 1)
        self.cache[(n, total)] = self.isSubsetSum(arr, total, n - 1) or self.isSubsetSum(arr, total - 2 * arr[n - 1], n - 1)
        return self.cache[(n, total)]
    
    def canPartition(self, nums: List[int]) -> bool:
        self.cache = {}
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        return self.isSubsetSum(nums, total, n)