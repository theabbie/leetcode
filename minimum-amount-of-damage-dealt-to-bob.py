import math
from functools import cmp_to_key

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        vals = [(damage[i], health[i]) for i in range(n)]
        def cmp(a, b):
            d0, h0 = a
            d1, h1 = b
            s0 = math.ceil(h0 / power)
            s1 = math.ceil(h1 / power)
            if (d0 + d1) * s0 + d1 * s1 >= (d0 + d1) * s1 + d0 * s0:
                return 1
            return -1
        vals.sort(key = cmp_to_key(cmp))
        s = sum(damage)
        res = 0
        for d, h in vals:
            sec = math.ceil(h / power)
            res += sec * s
            s -= d
        return res