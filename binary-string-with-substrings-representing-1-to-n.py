import random

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for _ in range(10000):
            k = random.randint(1, n)
            if "{:b}".format(k) not in s:
                return False
        return True