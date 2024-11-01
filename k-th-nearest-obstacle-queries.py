from sortedcontainers import SortedList

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = []
        d = SortedList()
        for x, y in queries:
            d.add(abs(x) + abs(y))
            res.append(d[k - 1] if len(d) >= k else -1)
        return res