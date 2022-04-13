class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        op = ""
        i = 0
        for c in s[::-1]:
            if c != "-":
                i += 1
                op = c.upper() + op
                if i % k == 0:
                    op = "-" + op
        if len(op) > 0 and op[0] == "-":
            op = op[1:]
        return op