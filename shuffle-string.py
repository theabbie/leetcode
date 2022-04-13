class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        op = ["" for i in range(n)]
        for i in range(n):
            op[indices[i]] = s[i]
        return "".join(op)