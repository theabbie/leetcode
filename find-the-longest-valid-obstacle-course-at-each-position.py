class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] = max(x[i], x[j])

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        mapped = {}
        curr = 0
        for el in sorted(obstacles):
            if el not in mapped:
                mapped[el] = curr
                curr += 1
        for i in range(n):
            obstacles[i] = mapped[obstacles[i]]
        n = len(obstacles)
        res = [1] * n
        fw = FenwickTree([0] * n)
        for i in range(n):
            res[i] = 1 + fw.query(obstacles[i] + 1)
            fw.update(obstacles[i], res[i])
        return res