class Solution:
    def prevlowest(self, arr, n):
        prevlow = [-1 for i in range(n)]
        stack = []
        for i in range(n):
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                curr = stack.pop()
            if len(stack) > 0:
                prevlow[i] = stack[-1]
            stack.append(i)
        return prevlow
    
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
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev = [self.prevlowest(matrix[i], n) for i in range(m)]
        mrec = 0
        for i in range(n):
            curr = self.largestRectangleArea([(i - prev[j][i]) if matrix[j][i] == "1" else 0 for j in range(m)])
            mrec = max(mrec, curr)
        return mrec