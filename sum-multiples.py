class Solution:
    def sumOfMultiples(self, n: int) -> int:
        val = lambda k: k * (n // k) * (n // k + 1) // 2
        return val(3) + val(5) + val(7) - val(15) - val(21) - val(35) + val(105)