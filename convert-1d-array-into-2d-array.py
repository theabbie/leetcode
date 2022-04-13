class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = len(original)
        if k != m * n:
            return []
        op = [[0 for i in range(n)] for i in range(m)]
        for i in range(k):
            op[i // n][i % n] = original[i]
        return op