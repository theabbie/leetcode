class Solution:
    def getexp(self, num, target, i, n, lastop, curr):
        if i >= n:
            x = "".join(curr)
            if eval(x) == target:
                self.res.append(x)
            return
        if lastop:
            self.getexp(num, target, i + 1, n, False, curr + [num[i]])
        else:
            if curr[-1] != "0":
                self.getexp(num, target, i + 1, n, False, curr[:-1] + [curr[-1] + num[i]])
            for op in "+-*":
                self.getexp(num, target, i, n, True, curr + [op])
    
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(set(num)) == 1 and num[0] != "0" and target % int(num[0]) != 0:
            return []
        self.res = []
        self.getexp(num, target, 0, len(num), True, [])
        return self.res