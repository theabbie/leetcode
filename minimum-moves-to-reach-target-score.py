class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = 0
        while target > 1 and maxDoubles > 0:
            n += 1 + target % 2
            target = target // 2
            maxDoubles -= 1
        return n + target - 1