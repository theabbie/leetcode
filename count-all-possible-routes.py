from collections import defaultdict
import bisect

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 10 ** 9 + 7
        n = len(locations)
        x = locations[start]
        y = locations[finish]
        locations.sort()
        start = locations.index(x)
        finish = locations.index(y)
        count = defaultdict(lambda: defaultdict(int))
        for f in range(fuel + 1):
            count[start][f] = 1
        for f in range(fuel + 1):
            for i in range(n):
                x = bisect.bisect_left(locations, locations[i] - f) - 1
                y = bisect.bisect_left(locations, locations[i] + f) + 1
                for j in range(max(x, 0), min(y, n)):
                    if i != j and f >= abs(locations[i] - locations[j]):
                        count[i][f] += count[j][f - abs(locations[i] - locations[j])]
                        count[i][f] %= M
        return count[finish][fuel]