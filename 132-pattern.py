class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        k = -1
        for i in range(n - 1, -1, -1):
            if k > -1 and nums[k] > nums[i]:
                return True
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                k = stack.pop()
            stack.append(i)
        return False

# class Solution:
#     def makeSeg(self, arr, i, j):
#         seg = self.seg
#         if (i, j) in seg:
#             return seg[(i, j)]
#         if i == j:
#             seg[(i, j)] = arr[i]
#             return arr[i]
#         mid = (i + j) // 2
#         curr = max(self.makeSeg(arr, i, mid), self.makeSeg(arr, mid + 1, j))
#         seg[(i, j)] = curr
#         return curr
    
#     def getMax(self, arr, i, j, ni, nj):
#         seg = self.seg
#         if ni >= i and nj <= j:
#             return seg[(ni, nj)]
#         if (ni < i and nj < i) or (ni > j and nj > j):
#             return float('-inf')
#         mid = (ni + nj) // 2
#         return max(self.getMax(arr, i, j, ni, mid), self.getMax(arr, i, j, mid + 1, nj))
    
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         self.seg = {}
#         self.makeSeg(nums, 0, n - 1)
#         for i in range(n):
#             for j in range(i + 2, n):
#                 if nums[j] > nums[i] and self.getMax(nums, i, j, 0, n - 1) > nums[j]:
#                     return True
#         return False

# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         next_lowest = [n for i in range(n)]
#         stack = []
#         for i in range(n):
#             while len(stack) > 0 and nums[i] < nums[stack[-1]]:
#                 curr = stack.pop()
#                 next_lowest[curr] = i
#                 for j in range(curr):
#                     if nums[j] < nums[i]:
#                         return True
#             stack.append(i)
#         return False

# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         currMin = float('inf')
#         currMax = float('-inf')
#         for num in nums:
#             currMin = min(currMin, num)
#             currMax = max(currMax, num)
#             if num > currMin and num < currMax:
#                 return True
#         return False