import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(rooms)
        q = len(queries)
        res = [-1] * q
        queries = [[queries[i][0], queries[i][1], i] for i in range(q)]
        queries.sort(key = lambda x: -x[1])
        rooms.sort(key = lambda x: -x[1])
        i = 0
        ids = []
        for p, s, pos in queries:
            while i < n and rooms[i][1] >= s:
                bisect.insort(ids, rooms[i][0])
                i += 1
            j = bisect.bisect_left(ids, p)
            curr = (float('inf'), -1)
            for k in [j - 1, j, j + 1]:
                if 0 <= k < len(ids):
                    curr = min(curr, (abs(p - ids[k]), ids[k]))
            res[pos] = curr[1]
        return res