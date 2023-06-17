class Solution:
    def smallest(self, s, i, n, k, tight, prev, prevprev, same, res):
        if i >= n:
            return not same
        key = (i, tight, prev, prevprev, same)
        if key in self.cache:
            return self.cache[key]
        minchar = 0
        if tight:
            minchar = ord(s[i]) - ord('a')
        for cc in range(minchar, k):
            c = chr(ord('a') + cc)
            if cc != prev and cc != prevprev:
                res[i] = c
                curr = self.smallest(s, i + 1, n, k, tight and cc == minchar, cc, prev, same and c == s[i], res)
                if curr:
                    self.cache[key] = True
                    return True
                res[i] = ""
        self.cache[key] = False
        return False
            
    
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        res = [""] * n
        self.cache = {}
        self.smallest(s, 0, n, k, True, -1, -1, True, res)
        return "".join(res)