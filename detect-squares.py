from collections import Counter

class DetectSquares:
    def __init__(self):
        self.ctr = Counter()

    def add(self, point: List[int]) -> None:
        self.ctr[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            mul = 1
            while 0 <= x + mul * dx <= 1000 and 0 <= y + mul * dy <= 1000:
                res += self.ctr[(x + mul * dx, y)] * self.ctr[(x, y + mul * dy)] * self.ctr[(x + mul * dx, y + mul * dy)]
                mul += 1
        return res