M = 10 ** 9 + 7

cache = {}

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def count(rem, pos):
            if rem == 0:
                return int(pos == 0)
            key = (rem, pos, arrLen)
            if key in cache:
                return cache[key]
            res = 0
            for i in range(pos - 1, pos + 2):
                if 0 <= i < arrLen:
                    res += count(rem - 1, i)
                    res %= M
            cache[key] = res
            return res
        return count(steps, 0)