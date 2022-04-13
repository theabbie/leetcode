class Solution:
    def trap(self, height: List[int]) -> int:
        h = max(height)
        n = len(height)
        blocks = sum(height)
        total = 0
        for i in range(h - 1, -1, -1):
            left = 0
            right = n - 1
            while height[left] <= i:
                left += 1
            while height[right] <= i:
                right -= 1
            total += right - left
        total -= (blocks - h)
        return total