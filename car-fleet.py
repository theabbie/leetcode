class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        prev = (float('inf'), float('inf'))
        res = n
        for i in range(n - 1, -1, -1):
            dist = prev[0] - cars[i][0]
            duration = cars[i][1] - prev[1]
            if duration * cars[i][0] + dist * cars[i][1] <= target * duration:
                res -= 1
            else:
                prev = cars[i]
        return res