class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = {(x, y) for x, y in guards}
        walls = {(x, y) for x, y in walls}
        res = set()
        for i in range(m):
            for order in [range(n), range(n - 1, -1, -1)]:
                active = False
                for j in order:
                    if (i, j) in guards:
                        active = True
                    elif (i, j) in walls:
                        active = False
                    elif active:
                        res.add((i, j))
        for j in range(n):
            for order in [range(m), range(m - 1, -1, -1)]:
                active = False
                for i in order:
                    if (i, j) in guards:
                        active = True
                    elif (i, j) in walls:
                        active = False
                    elif active:
                        res.add((i, j))
        return m * n - len(guards) - len(walls) - len(res)