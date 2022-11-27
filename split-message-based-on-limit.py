class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        for l in range(1, 6):
            M = 10 ** l
            off = 3 + l
            i = 0
            j = 1
            while i < n and j < M:
                k = max(limit - off - len(str(j)), 0)
                i += k
                j += 1
            j -= 1
            if i >= n:
                res = []
                curr = 0
                for x in range(1, j + 1):
                    suff = f"<{x}/{j}>"
                    k = limit - len(suff)
                    res.append(message[curr:curr+k] + suff)
                    curr += k
                return res
        return []