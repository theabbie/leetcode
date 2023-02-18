class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for el in costs:
            if coins >= el:
                res += 1
                coins -= el
        return res