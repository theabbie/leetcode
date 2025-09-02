import builtins

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        builtins.pow = cache(builtins.pow)
        @cache
        def c(x, mn):
            if x == 0:
                return True
            y = mn
            while x >= pow(3, y):
                if c(x - pow(3, y), y + 1):
                    return True
                y += 1
            return False
        return c(n, 0)