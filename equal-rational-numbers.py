class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def add(self, x, y):
        up = x[0] * y[1] + x[1] * y[0]
        down = x[1] * y[1]
        mul = self.gcd(up, down)
        return (up // mul, down // mul)
    
    def getval(self, x):
        if "." not in x:
            x += "."
        a, b = x.split(".")
        a = (int(a), 1)
        c = d = (0, 1)
        if "(" in b:
            i = b.index("(")
            j = b.index(")")
            if i > 0:
                c = (int(b[:i]), pow(10, i))
            d = (int(b[i+1:j]), pow(10, i) * (pow(10, j - i - 1) - 1))
        elif len(b) > 0:
            c = (int(b), pow(10, len(b)))
        return self.add(a, self.add(c, d))
    
    def isRationalEqual(self, s: str, t: str) -> bool:
        return self.getval(s) == self.getval(t)
        