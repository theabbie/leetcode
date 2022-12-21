import math

class Solution:
    def smallestValue(self, n: int) -> int:
        prev = n
        i = 2
        newval = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                n = n // i
                newval += i
        if n > 1:
            newval += n
        if newval == prev:
            return newval
        return self.smallestValue(newval)