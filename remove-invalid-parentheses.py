from collections import deque

class Solution:
    def isValid(self, s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            if c == ')':
                if ctr == 0:
                    return False
                ctr -= 1
        return ctr == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = deque([(s, 0)])
        v = {s}
        minlen = float('inf')
        res = []
        while len(q) > 0:
            curr, l = q.pop()
            if self.isValid(curr):
                minlen = min(minlen, l)
                if l == minlen:
                    res.append(curr)
            if l < minlen:
                n = len(curr)
                for i in range(n):
                    newstr = curr[:i] + curr[i+1:]
                    if newstr not in v:
                        v.add(newstr)
                        q.appendleft((newstr, l + 1))
        return res