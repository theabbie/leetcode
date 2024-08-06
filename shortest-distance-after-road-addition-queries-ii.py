from sortedcontainers import SortedList

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        invs = SortedList()
        res = []
        s = 0
        for l, r in queries:
            x = invs.bisect_left((l, float('-inf')))
            if (0 <= x - 1 < len(invs) and invs[x - 1][1] >= r) or (0 <= x < len(invs) and invs[x][0] <= l and invs[x][1] >= r):
                res.append(n - 1 - s)
                continue
            while x < len(invs) and invs[x][0] >= l and invs[x][1] <= r:
                xx, yy = invs.pop(x)
                s -= yy - xx - 1
            invs.add((l, r))
            s += r - l - 1
            res.append(n - 1 - s)
        return res