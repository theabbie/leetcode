M = 10 ** 9 + 7

board = """"123
456
789
*0#""".split("\n")

m = 4
n = 3

cache = {}

def count(i, j, rem):
    if board[i][j] in "*#":
        return 0
    if rem == 1:
        return 1
    key = (i, j, rem)
    if key in cache:
        return cache[key]
    res = 0
    for dx in [-2, -1, 1, 2]:
        for dy in [-2, -1, 1, 2]:
            if abs(dx) == abs(dy):
                continue
            if 0 <= i + dx < m and 0 <= j + dy < n:
                res += count(i + dx, j + dy, rem - 1)
                res %= M
    cache[key] = res
    return res

class Solution:
    def knightDialer(self, moves: int) -> int:
        res = 0
        for i in range(m):
            for j in range(n):
                res += count(i, j, moves)
                res %= M
        return res