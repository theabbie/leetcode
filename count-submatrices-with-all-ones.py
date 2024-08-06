class Solution:
    def numSubmat(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = 0
        heights = [0] * n
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        for i in range(m):
            stack = []
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
                while len(stack) > 0 and heights[j] < heights[stack[-1]]:
                    curr = stack.pop()
                    next_smaller[curr] = j
                prev_smaller[j] = -1
                if len(stack) > 0:
                    prev_smaller[j] = stack[-1]
                stack.append(j)
            while len(stack) > 0:
                next_smaller[stack.pop()] = n
            for j in range(n):
                l = prev_smaller[j]
                r = next_smaller[j]
                res += (j - l) * (r - j) * heights[j]
        return res