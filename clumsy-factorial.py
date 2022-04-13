class Solution:
    def clumsy(self, n: int) -> int:
        expr = ""
        opr = ["*", "//", "+", "-"]
        for i in range(n):
            expr += str(n - i)
            if i < n - 1:
                expr += opr[i % 4]
        return eval(expr)