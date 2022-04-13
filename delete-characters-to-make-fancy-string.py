class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        i = 0
        dels = set()
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                if ctr > 2:
                    dels.add(i)
                i += 1
            i += 1
        return "".join([s[i] for i in range(n) if i not in dels])