from sortedcontainers import SortedList
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted([(queries[i], i) for i in range(len(queries))])
        res = [-1] * len(queries)
        i = 0
        ends = []
        lens = SortedList()
        for q, qpos in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(ends, (intervals[i][1], intervals[i][1] - intervals[i][0] + 1))
                lens.add(intervals[i][1] - intervals[i][0] + 1)
                i += 1
            while ends and ends[0][0] < q:
                lens.remove(heapq.heappop(ends)[1])
            if lens:
                res[qpos] = lens[0]
        return res