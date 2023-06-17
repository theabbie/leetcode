class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = (float('-inf'), float('inf'))
        for i in range(m):
            res = max(res, (mat[i].count(1), -i))
        return [-res[1], res[0]]