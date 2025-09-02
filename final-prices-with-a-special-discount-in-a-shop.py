class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, el in enumerate(prices):
            while stack and el <= prices[stack[-1]]:
                prices[stack.pop()] -= el
            stack.append(i)
        return prices