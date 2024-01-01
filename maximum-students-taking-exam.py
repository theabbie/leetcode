class Solution:
    def shift(self, mask, l, sb):
        mask &= ~(1 << l - 1)
        mask <<= 1
        if sb:
            mask |= 1
        return mask
    
    def check(self, seats, i, j, m, n):
        for dx, dy in [(0, -1), (-1, -1), (-1, 1)]:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and seats[x][y] == "S":
                return False
        return True
    
    def maxcount(self, seats, i, j, m, n, mask):
        if i >= m:
            return 0
        key = (i, j, mask)
        if key in self.cache:
            return self.cache[key]
        newi = i
        newj = j + 1
        if newj == n:
            newi += 1
            newj = 0
        res = self.maxcount(seats, newi, newj, m, n, self.shift(mask, n + 1, False))
        if seats[i][j] == "." and self.check(seats, i, j, m, n):
            seats[i][j] = "S"
            res = max(res, 1 + self.maxcount(seats, newi, newj, m, n, self.shift(mask, n + 1, True)))
            seats[i][j] = "."
        self.cache[key] = res
        return res
    
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.cache = {}
        return self.maxcount(seats, 0, 0, len(seats), len(seats[0]), 0)