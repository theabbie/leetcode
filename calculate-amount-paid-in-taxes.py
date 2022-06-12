class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        rem = income
        tax = 0
        prev = 0
        for b, p in brackets:
            if income >= b:
                tax += (b - prev) * p
                rem -= (b - prev)
                prev = b
            elif rem > 0:
                tax += rem * p
                rem = 0
                break
        return tax / 100