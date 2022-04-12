class Solution:
    def getInt(self, s):
        if len(s) == 0:
            return 1
        return int(s)
    
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split("+")
        minVal = float('inf')
        m = len(a)
        n = len(b)
        minPos = None
        for i in range(m):
            for j in range(1, n + 1):
                currVal = self.getInt(a[:i]) * (self.getInt(a[i:]) + self.getInt(b[:j])) * self.getInt(b[j:])
                if currVal < minVal:
                    minVal = currVal
                    minPos = (i, j)
        i , j = minPos
        return "{}({}+{}){}".format(a[:i], a[i:], b[:j], b[j:])