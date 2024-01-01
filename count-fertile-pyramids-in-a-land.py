class Solution:
    def count(self, arr):
        n = len(arr)
        res = 0
        stack = [(float('-inf'), n)]
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] >= arr[i] - i:
                stack.pop()
            stack.append((arr[i] - i, i))
            beg = 0
            end = len(stack) - 1
            j = i
            while beg <= end:
                mid = (beg + end) // 2
                if stack[mid][0] < -i:
                    j = stack[mid][1]
                    beg = mid + 1
                else:
                    end = mid - 1
            if j > i + 1:
                res += j - i - 1
        return res
    
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        estate = [[float('inf')] * n for _ in range(m)]
        res = 0
        for i in range(m):
            ones = 0
            for j in range(n):
                estate[i][j] = min(estate[i][j], ones)
                if grid[i][j] == 1:
                    ones += 1
                else:
                    ones = 0
                    estate[i][j] = float('-inf')
            ones = 0
            for j in range(n - 1, -1, -1):
                estate[i][j] = min(estate[i][j], ones)
                if grid[i][j] == 1:
                    ones += 1
                else:
                    ones = 0
                    estate[i][j] = float('-inf')
        for j in range(n):
            res += self.count([estate[i][j] for i in range(m)])
            res += self.count([estate[i][j] for i in range(m - 1, -1, -1)])
        return res