class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        stack = []
        for x, y in stockPrices:
            if len(stack) < 2:
                stack.append((x, y))
            else:
                ppx, ppy = stack[-2]
                px, py = stack[-1]
                if (py - ppy) * (x - px) == (px - ppx) * (y - py):
                    stack.pop()
                stack.append((x, y))
        return len(stack) - 1