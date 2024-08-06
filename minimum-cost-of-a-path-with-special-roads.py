import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads.append(target + target + [0])
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while len(heap) > 0:
            currdist, x, y = heapq.heappop(heap)
            for a, b, c, d, cost in specialRoads:
                if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))
        return dist[(target[0], target[1])]