class Solution:
    def findNthDigit(self, n: int) -> int:
        prevcumsum = None
        cumsum = 0
        l = 1
        while n >= cumsum:
            prevcumsum = cumsum
            nextcumsum = cumsum + 9 * l * (10 ** (l - 1))
            if nextcumsum >= n:
                break
            cumsum = nextcumsum
            l += 1
        n -= prevcumsum
        k, n = divmod(n - 1, l)
        num = str(10 ** (l - 1) + k)
        return int(num[n])