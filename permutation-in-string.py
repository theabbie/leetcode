class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        np = len(p)
        ns = len(s)
        op = []
        if np > ns:
            return op
        pctr = [0] * 26
        for c in p:
            pctr[ord(c) - ord('a')] += 1
        sctr = [0] * 26
        for i in range(np):
            sctr[ord(s[i]) - ord('a')] += 1
        i = 0
        while i < ns - np:
            if pctr == sctr:
                return True
            sctr[ord(s[i]) - ord('a')] -= 1
            sctr[ord(s[i + np]) - ord('a')] += 1
            i += 1
        if pctr == sctr:
            return True
        return False