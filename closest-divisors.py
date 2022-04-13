class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        closest = (1, num + 1)
        for x in [num + 1, num + 2]:
            curr = (1, x)
            i = 2
            while i * i <= x:
                if x % i == 0:
                    curr = (i, x // i)
                    if curr[1] - curr[0] < closest[1] - closest[0]:
                        closest = curr
                i += 1
        return closest