class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ctr = 0
        done = {}
        for w in words:
            if w in done:
                if done[w]:
                    ctr += 1
                continue
            if len(w) <= len(s) and self.isSubsequence(w, s):
                done[w] = True
                ctr += 1
            else:
                done[w] = False
        return ctr