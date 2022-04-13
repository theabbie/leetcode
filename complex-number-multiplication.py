class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1.split("+")
        c, d = num2.split("+")
        a = int(a)
        b = int(b[:-1])
        c = int(c)
        d = int(d[:-1])
        return "{}+{}i".format(a*c-b*d, a*d+b*c)