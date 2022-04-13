class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        slist = []
        tlist = []
        i = 0
        for c in s:
            if c not in smap:
                smap[c] = i
                i += 1
            slist.append(smap[c])
        i = 0
        for c in t:
            if c not in tmap:
                tmap[c] = i
                i += 1
            tlist.append(tmap[c])
        return slist == tlist