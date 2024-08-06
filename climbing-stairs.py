res = [1, 1, 2]

for _ in range(43):
    res.append(res[-2] + res[-1])

class Solution:
    def climbStairs(self, n: int) -> int:
        return res[n]