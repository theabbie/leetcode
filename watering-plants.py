class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        i = 0
        water = capacity
        steps = 0
        while i < n:
            if water >= plants[i]:
                water -= plants[i]
                i += 1
                steps += 1
            else:
                steps += 2 * i
                water = capacity
        return steps