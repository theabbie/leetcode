class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        rem = n % 7
        return 28 * k + 7 * k * (k - 1) // 2 + k * rem + rem * (rem + 1) // 2