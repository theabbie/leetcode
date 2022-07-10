class Solution:
    def getStats(self, s):
        rel = ""
        ctr = 0
        prefl = []
        prefr = []
        for c in s:
            if c != "_":
                rel += c
                if c == "L":
                    prefl.append(ctr)
                else:
                    prefr.append(ctr)
            else:
                ctr += 1
        return [rel, ctr, prefl, prefr]
    
    def canChange(self, start: str, target: str) -> bool:
        rels, ctrs, sprefl, sprefr = self.getStats(start)
        relt, ctrt, tprefl, tprefr = self.getStats(target)
        if rels != relt or ctrs != ctrt or len(sprefl) != len(tprefl) or len(sprefr) != len(tprefr):
            return False
        m = len(sprefl)
        for i in range(m):
            if tprefl[i] > sprefl[i]:
                return False
        n = len(sprefr)
        for i in range(n):
            if tprefr[i] < sprefr[i]:
                return False
        return True