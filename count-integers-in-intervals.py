from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.L = 1
        self.R = 10 ** 9
        self.parts = SortedList()
        self.res = 0
        
    def split(self, x, y, i, j):
        if y < i or x > j:
            return []
        if x >= i and y <= j:
            return [(x, y)]
        mid = (x + y) // 2
        return self.split(x, mid, i, j) + self.split(mid + 1, y, i, j)

    def add(self, left: int, right: int) -> None:
        for l, r in self.split(self.L, self.R, left, right):
            x = self.parts.bisect_right((l, float('inf'))) - 1
            if 0 <= x < len(self.parts) and self.parts[x][1] >= r:
                continue
            x = self.parts.bisect_left((l, float('-inf')))
            while x < len(self.parts) and self.parts[x][1] <= r:
                rm = self.parts.pop(x)
                self.res -= rm[1] - rm[0] + 1
            self.parts.add((l, r))
            self.res += r - l + 1

    def count(self) -> int:
        return self.res