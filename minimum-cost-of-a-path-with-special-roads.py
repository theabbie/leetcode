import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = [[a, b, c, d, x] for a, b, c, d, x in specialRoads if x < abs(a - c) + abs(b - d)]
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while len(heap) > 0:
            currdist, x, y = heapq.heappop(heap)
            for a, b, c, d, cost in specialRoads:
                if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))
        res = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for a, b, c, d, cost in specialRoads:
            res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))
        return res