class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        res = 0
        rooks.sort(key = lambda p: p[0])
        for i in range(len(rooks)):
            res += abs(i - rooks[i][0])
        rooks.sort(key = lambda p: p[1])
        for i in range(len(rooks)):
            res += abs(i - rooks[i][1])
        return res