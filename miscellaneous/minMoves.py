class Solution:
    def minMovesRec(self, target, maxDoubles):
        if target < 1 or maxDoubles < 0:
            return float('inf')
        if target == 1:
            return 0
        if (target, maxDoubles) in self.cache:
            return self.cache[(target, maxDoubles)]
        if target % 2 == 0:
            curr = min(1 + self.minMovesRec(target - 1, maxDoubles), 1 + self.minMovesRec(target // 2, maxDoubles - 1))
        else:
            curr = 1 + self.minMovesRec(target - 1, maxDoubles)
        self.cache[(target, maxDoubles)] = curr
        return curr
    
    def minMoves(self, target: int, maxDoubles: int) -> int:
        self.cache = {}
        return self.minMovesRec(target, maxDoubles)

print(Solution().minMoves(766972377, 92))