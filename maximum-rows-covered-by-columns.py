class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m = len(mat)
        n = len(mat[0])
        res = 0
        for i in range(1 << n):
            ctr = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    ctr += 1
            if ctr == cols:
                curr = 0
                for x in range(m):
                    covered = True
                    for y in range(n):
                        if mat[x][y] == 1 and (i & (1 << y)) == 0:
                            covered = False
                            break
                    if covered:
                        curr += 1
                res = max(res, curr)
        return res