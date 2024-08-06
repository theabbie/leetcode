from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q = deque([(x, 0)])
        v = {x}
        while len(q) > 0:
            curr, steps = q.pop()
            if curr == y:
                return steps
            if curr % 11 == 0 and (curr // 11) not in v:
                v.add(curr // 11)
                q.appendleft((curr // 11, steps + 1))
            if curr % 5 == 0 and (curr // 5) not in v:
                v.add(curr // 5)
                q.appendleft((curr // 5, steps + 1))
            if (curr + 1) not in v:
                v.add(curr + 1)
                q.appendleft((curr + 1, steps + 1))
            if curr > 1 and (curr - 1) not in v:
                v.add(curr - 1)
                q.appendleft((curr - 1, steps + 1))