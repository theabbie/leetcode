class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = len(original)
        if k != m * n:
            return []
        for i in range(m):
            original.extend([original[i * n : (i + 1) * n]])
        return original[k:]