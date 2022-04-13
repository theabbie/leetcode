class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_lowest = [n for i in range(n)]
        prev_lowest = [-1 for i in range(n)]
        maxArea = 0
        inc_stack = []
        for i in range(n):
            while len(inc_stack) > 0 and heights[i] < heights[inc_stack[-1]]:
                curr = inc_stack.pop()
                next_lowest[curr] = i
            if len(inc_stack) > 0:
                prev_lowest[i] = inc_stack[-1]
            inc_stack.append(i)
        for i in range(n):
            currArea = (next_lowest[i] - prev_lowest[i] - 1) * heights[i]
            maxArea = max(maxArea, currArea)
        return maxArea
        
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         maxArea = 0
#         for i in range(n):
#             curr = heights[i]
#             left = i
#             right = i
#             while left >= 0 and heights[left] >= curr:
#                 left -= 1
#             left += 1
#             while right < n and heights[right] >= curr:
#                 right += 1
#             right -= 1
#             maxArea = max(maxArea, curr * (right - left + 1))
#         return maxArea
        
# class Solution:
#     def makeSeg(self, arr, i, j):
#         if (i, j) in self.seg:
#             return self.seg[(i, j)]
#         if i == j:
#             self.seg[(i, j)] = arr[i]
#             return arr[i]
#         mid = (i + j) // 2
#         curr = min(self.makeSeg(arr, i, mid), self.makeSeg(arr, mid + 1, j))
#         self.seg[(i, j)] = curr
#         return curr
    
#     def getMin(self, arr, i, j, ni, nj):
#         if ni >= i and nj <= j:
#             return self.seg[(ni, nj)]
#         if (ni < i and nj < i) or (ni > j and nj > j):
#             return float('inf')
#         mid = (ni + nj) // 2
#         return min(self.getMin(arr, i, j, ni, mid), self.getMin(arr, i, j, mid + 1, nj))
    
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         self.seg = {}
#         n = len(heights)
#         if n == 1:
#             return heights[0]
#         self.makeSeg(heights, 0, n - 1)
#         mrec = float('-inf')
#         for i in range(n):
#             for j in range(i, n):
#                 mrec = max(mrec, (j - i + 1) * self.getMin(heights, i, j, 0, n - 1))
#         return mrec

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         areas = []
#         maxArea = float('-inf')
#         areas.append((0, heights[0]))
#         for i in range(1, n):
#             if heights[i] < areas[-1][1]:
#                 maxArea = max(maxArea, (i - areas[-1][0]) * areas[-1][1])
#                 areas.pop()
#             areas.append((i, heights[i]))
#         return maxArea