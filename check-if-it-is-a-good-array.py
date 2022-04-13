class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            curr = self.gcd(curr, nums[i])
            if curr == 1:
                return True
        return curr == 1

# class Solution:
#     def gcd(self, a, b):
#         while b:
#             a, b = b, a % b
#         return a
    
#     def isGoodArray(self, nums: List[int]) -> bool:
#         n = len(nums)
#         paths = [([i], nums[i]) for i in range(n)]
#         i = 0
#         while i < len(paths):
#             curr, currgcd = paths[i]
#             if currgcd == 1:
#                 return True
#             for j in range(curr[-1] + 1, n):
#                 paths.append((curr + [j], self.gcd(currgcd, nums[j])))
#             i += 1
#         return False