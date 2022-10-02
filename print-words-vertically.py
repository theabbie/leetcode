class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max([len(w) for w in words])
        res = [[] for _ in range(n)]
        for w in words:
            for i in range(n):
                if i < len(w):
                    res[i].append(w[i])
                else:
                    res[i].append(" ")
        return ["".join(row).rstrip() for row in res]