class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        l = 1
        res = 0
        while l * (l - 1) // 2 < n:
            rem = n - l * (l - 1) // 2
            if rem % l == 0:
                res += 1
            l += 1
        return res