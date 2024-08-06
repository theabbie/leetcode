from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()
        for i in range(n):
            q.appendleft((tickets[i], i))
        t = 0
        while q:
            t += 1
            c, pos = q.pop()
            c -= 1
            if c > 0:
                q.appendleft((c, pos))
            elif pos == k:
                return t