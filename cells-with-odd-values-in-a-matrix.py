class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cols = [0] * n
        rows = [0] * m
        ctr = 0
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        for i in range(n):
            for j in range(m):
                if (cols[i] + rows[j]) % 2 == 1:
                    ctr += 1
        return ctr