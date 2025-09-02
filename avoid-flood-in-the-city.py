import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        last = {}
        for i in range(n):
            if rains[i] != 0:
                last[rains[i]] = i
        res = []
        full = []
        fullset = set()
        for i in range(n):
            if rains[i] != 0:
                if rains[i] in fullset:
                    return []
                fullset.add(rains[i])
                heapq.heappush(full, (last.get(rains[i], float('inf')), rains[i]))
                res.append(-1)
            else:
                if full:
                    v, x = heapq.heappop(full)
                    fullset.remove(x)
                    res.append(x)
                else:
                    res.append(1)
            while full and full[0][0] <= i:
                heapq.heappop(full)
        return res