class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        np = len(p)
        ns = len(s)
        if np > ns:
            return []
        pctr = [0] * 26
        for c in p:
            pctr[ord(c) - ord('a')] += 1
        sctr = [0] * 26
        for i in range(np):
            sctr[ord(s[i]) - ord('a')] += 1
        op = []
        i = 0
        while i < ns - np:
            if pctr == sctr:
                op.append(i)
            sctr[ord(s[i]) - ord('a')] -= 1
            sctr[ord(s[i + np]) - ord('a')] += 1
            i += 1
        if pctr == sctr:
            op.append(i)
        return op