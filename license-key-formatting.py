class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        op = []
        n = len(s)
        i = 0
        for c in range(n - 1, -1, -1):
            if s[c] != "-":
                i += 1
                op.append(s[c].upper())
                if i % k == 0:
                    op.append("-")
        if len(op) > 0 and op[-1] == "-":
            op.pop()
        op.reverse()
        return "".join(op)