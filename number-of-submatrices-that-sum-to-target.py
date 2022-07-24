from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j + 1] = prefix[i][j] + matrix[i][j]
        for i in range(n):
            for j in range(i, n):
                seen = defaultdict(int)
                curr = 0
                seen[0] = 1
                for k in range(m):
                    curr += prefix[k][j + 1] - prefix[k][i]
                    if curr - target in seen:
                        res += seen[curr - target]
                    seen[curr] += 1
        return res