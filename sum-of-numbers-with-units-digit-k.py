class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        d = num % 10
        for n in range(1, num + 1):
            if (k * n) % 10 == d:
                newnum = num - k * n
                if newnum >= 0 and newnum % 10 == 0:
                    return n
        return -1