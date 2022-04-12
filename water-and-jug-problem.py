class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        init = (0, 0)
        paths = [init]
        visited = {init}
        i = 0
        while i < len(paths):
            a, b = paths[i]
            if a == targetCapacity or b == targetCapacity or a + b == targetCapacity:
                return True
            opts = [(jug1Capacity, b), (a, jug2Capacity), (jug1Capacity, jug2Capacity), (0, b), (a, 0), (min(a + b, jug1Capacity), max(b - (jug1Capacity - a), 0)), (max(a - (jug2Capacity - b), 0), min(b + a, jug2Capacity))]
            for opt in opts:
                if opt not in visited:
                    visited.add(opt)
                    paths.append(opt)
            i += 1
        return False