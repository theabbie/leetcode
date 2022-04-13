class Solution:
    def trap(self, height: List[int]) -> int:
        blocks = 0
        n = 0
        h = float('-inf')
        for hh in height:
            blocks += hh
            n += 1
            h = max(h, hh)
        total = 0
        left = 0
        right = n - 1
        for i in range(h):
            while height[left] <= i:
                left += 1
            while height[right] <= i:
                right -= 1
            total += right - left
        total -= (blocks - h)
        return total