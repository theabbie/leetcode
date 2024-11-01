class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda p: p[0])
        @lru_cache(maxsize = None)
        def dp(i, j):
            if i >= len(robot):
                return 0
            if j >= len(factory):
                return float('inf')
            res = dp(i, j + 1)
            cost = 0
            for x in range(i, min(i + factory[j][1], len(robot))):
                cost += abs(robot[x] - factory[j][0])
                res = min(res, cost + dp(x + 1, j + 1))
            return res
        return dp(0, 0)