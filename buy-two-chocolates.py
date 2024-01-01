class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = float('inf'), float('inf')
        for el in prices:
            a, b, temp = sorted([a, b, el])
        if a + b > money:
            return money
        return money - a - b