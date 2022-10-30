class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        d = set(dictionary)
        for q in queries:
            found = False
            for w in d:
                n = len(w)
                ctr = 0
                for i in range(n):
                    if w[i] != q[i]:
                        ctr += 1
                if ctr <= 2:
                    found = True
                    break
            if found:
                res.append(q)
        return res