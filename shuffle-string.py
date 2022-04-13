class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        op = " " * n
        for i in range(n):
            op = op[: indices[i]] + s[i] + op[indices[i] + 1 :]
        return op