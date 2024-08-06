class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        l = 1
        while l * (l + 1) // 2 <= n:
            if (n - l * (l - 1) // 2) % l == 0:
                res += 1
            l += 1
        return res