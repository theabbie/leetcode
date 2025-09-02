import math

def ops(l, r):
    total = 0
    m = 0
    start = l
    k = 1
    while True:
        low = 4 ** (k - 1)
        high = 4 ** k - 1
        if low > r:
            break
        a = max(start, low)
        b = min(r, high)
        if a <= b:
            cnt = b - a + 1
            total += k * cnt
            m = k
        k += 1
    b1 = m
    b2 = math.ceil(total / 2)
    return max(b1, b2)

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        return sum(ops(l, r) for l, r in queries)