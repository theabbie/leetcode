class Stack:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.pi = [0] * self.n
        for i in range(1, self.n):
            j = self.pi[i - 1]
            while j and s[i] != s[j]:
                j = self.pi[j - 1]
            if s[i] == s[j]:
                j += 1
            self.pi[i] = j
        self.stack = []
        self.state = 0
    def push(self, c):
        v = self.state
        while v > 0 and (v == self.n or self.s[v] != c):
            v = self.pi[v - 1]
        if v < self.n and self.s[v] == c:
            v += 1
        self.state = v
        self.stack.append((c, v))
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.state = self.stack[-1][1] if self.stack else 0
    def query(self):
        return self.state

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = Stack(part)
        for c in s:
            res.push(c)
            if res.query() == len(part):
                for _ in range(len(part)):
                    res.pop()
        return "".join(c[0] for c in res.stack)