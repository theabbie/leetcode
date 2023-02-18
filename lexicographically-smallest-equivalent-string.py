class Solution:
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px
            self.minchar[px] = min(self.minchar[px], self.minchar[py])
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        pos = lambda c: ord(c) - ord('a')
        char = lambda x: chr(ord('a') + x)
        self.parent = list(range(26))
        self.minchar = list(range(26))
        for i in range(n):
            self.union(pos(s1[i]), pos(s2[i]))
        return "".join(char(self.minchar[self.find(pos(c))]) for c in baseStr)