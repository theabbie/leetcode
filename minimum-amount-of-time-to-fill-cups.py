class Solution:
    def fillCups(self, amount: List[int]) -> int:
        t = 0
        amount.sort()
        while amount != [0, 0, 0]:
            if amount[2] > 0 and amount[1] > 0:
                amount[1] -= 1
                amount[2] -= 1
            elif amount[2] > 0:
                amount[2] -= 1
            amount.sort()
            t += 1
        return t