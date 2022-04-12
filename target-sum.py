class Solution:
    def findways(self, nums: List[int], target: int, n, i) -> int:
        ways = 0
        if i >= n:
            return ways
        if (target, i) in self.cache:
            return self.cache[(target, i)]
        if i == n - 1:
            if nums[i] == target:
                ways += 1
            if nums[i] == -target:
                ways += 1
        ways += self.findways(nums, target + nums[i], n, i + 1)
        ways += self.findways(nums, target - nums[i], n, i + 1)
        self.cache[(target, i)] = ways
        return ways
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        return self.findways(nums, target, len(nums), 0)

# class Solution:
#     def isSubsetSum(self, arr, total, n):
#         if total == 0:
#             return True
#         if total != 0 and n == 0:
#             return False
#         if (n, total) in self.cache:
#             return self.cache[(n, total)]
#         if 2 * arr[n - 1] > total:
#             return self.isSubsetSum(arr, total, n - 1)
#         self.cache[(n, total)] = self.isSubsetSum(arr, total, n - 1) or self.isSubsetSum(arr, total - 2 * arr[n - 1], n - 1)
#         return self.cache[(n, total)]
    
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         ctr = 0
#         paths = [(nums[0], 0)]
#         while len(paths) > 0:
#             val, i = paths.pop(0)
#             if val == target:
#                 ctr += 1
#             if i < n - 1:
#                 paths.append((val + nums[i + 1], i + 1))
#                 paths.append((val - nums[i + 1], i + 1))
#         return ctr

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         ctr = 0
#         total = sum(nums)
#         k = (total + target) // 2
#         sums = [(num, i) for i, num in enumerate(nums)]
#         while len(sums) > 0:
#             curr, i = sums.pop(0)
#             if curr == k:
#                 ctr += 1
#             for j in range(i + 1, n):
#                 if curr + nums[j] <= k:
#                     sums.append((curr + nums[j], j))
#         return ctr