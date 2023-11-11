class Solution:
    def sort(self, s):
        n = len(s)
        s = list(s)
        vals = [[], []]
        for i in range(n):
            vals[i % 2].append(s[i])
        vals[0].sort(reverse = True)
        vals[1].sort(reverse = True)
        for i in range(n):
            s[i] = vals[i % 2].pop()
        return "".join(s)
    
    def checkStrings(self, s1: str, s2: str) -> bool:
        return self.sort(s1) == self.sort(s2)