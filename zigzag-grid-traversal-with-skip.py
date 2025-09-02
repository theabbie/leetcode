class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        f = True
        for r in grid:
            res.extend(r if f else r[::-1])
            f = not f
        return [res[i] for i in range(0, len(res), 2)]