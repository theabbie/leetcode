class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        m = len(horizontalCuts)
        n = len(verticalCuts)
        a = max(horizontalCuts[i+1] - horizontalCuts[i] for i in range(m-1))
        b = max(verticalCuts[i+1] - verticalCuts[i] for i in range(n-1))
        return (a * b) % (10 ** 9 + 7)