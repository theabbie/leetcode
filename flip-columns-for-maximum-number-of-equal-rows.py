class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ctr = Counter()
        for r in matrix:
            r = min(r, [1 - x for x in r])
            ctr[tuple(r)] += 1
        return max(ctr.values())
            