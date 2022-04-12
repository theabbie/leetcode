class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        mvol = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            mvol = max(mvol, (j - i) * min(height[i], height[j]))
        return mvol