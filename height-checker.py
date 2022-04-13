class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        expected = sorted(heights)
        return len([i for i in range(n) if heights[i] != expected[i]])