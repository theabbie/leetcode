class Solution:
    def parse(self, s):
        vals = [0, 0]
        chunk = ""
        sign = 1
        for c in s:
            if c == "+" or c == "-" or c == "s":
                if len(chunk) > 0:
                    if chunk[-1] == "x":
                        coefficient = chunk[:-1]
                        if not coefficient:
                            coefficient = "1"
                        vals[0] += sign * int(coefficient)
                    else:
                        vals[1] += sign * int(chunk)
                    chunk = ""
                if c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
            else:
                chunk += c
        return vals
    
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split("=")
        lvals = self.parse(l + "s")
        rvals = self.parse(r + "s")
        numer = rvals[1] - lvals[1]
        denom = lvals[0] - rvals[0]
        if denom != 0:
            return "x={}".format(numer // denom)
        if numer != 0:
            return "No solution"
        return "Infinite solutions"