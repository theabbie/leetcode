class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ctr = [Counter() for _ in range(n)]
        for x, y in pick:
            ctr[x][y] += 1
        return len([i for i in range(n) if len(ctr[i]) > 0 and max(ctr[i].values()) > i])