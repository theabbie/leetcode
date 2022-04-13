class Solution:
    def keygen(self, s):
        smap = {}
        slist = []
        i = 0
        for c in s:
            if c not in smap:
                smap[c] = i
                i += 1
            slist.append(smap[c])
        return slist
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        plist = self.keygen(pattern)
        return [w for w in words if self.keygen(w) == plist]