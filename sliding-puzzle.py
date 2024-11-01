from collections import deque

start = (1,2,3,4,5,0)
q = deque([(start, 0)])
v = {start}
res = {}
while q:
    curr, d = q.pop()
    res[curr] = d
    pos = curr.index(0)
    i, j = pos // 3, pos % 3
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < 2 and 0 <= y < 3:
            newcurr = list(curr)
            newcurr[pos], newcurr[3 * x + y] = newcurr[3 * x + y], newcurr[pos]
            newcurr = tuple(newcurr)
            if newcurr not in v:
                v.add(newcurr)
                q.appendleft((newcurr, d + 1))

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        return res.get(tuple(board[0] + board[1]), -1)