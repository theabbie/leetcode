from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        matmask = 0
        for i in range(m * n):
            if mat[i // n][i % n] == 1:
                matmask ^= (1 << i)
        v = {matmask}
        q = deque([(matmask, 0)])
        while len(q) > 0:
            curr, steps = q.pop()
            if curr == 0:
                return steps
            for i in range(m):
                for j in range(n):
                    currmask = curr 
                    for x, y in [(i, j), (i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n:
                            currmask ^= (1 << (n * x + y))
                    if currmask not in v:
                        v.add(currmask)
                        q.appendleft((currmask, steps + 1))
        return -1