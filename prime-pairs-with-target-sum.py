class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        N = 1 + n
        sp = [1] * N
        v = [False] * N
        for i in range(2, N, 2):
            sp[i] = 2
        for i in range(3, N, 2):
            if not v[i]:
                sp[i] = i
                j = i
                while j * i < N:
                    v[j * i] = True
                    sp[j * i] = i
                    j += 2
        plist = [i for i in range(2, n + 1) if sp[i] == i]
        res = []
        seen = set()
        for p in plist:
            seen.add(p)
            if n - p in seen:
                res.append((n - p, p))
        res.sort()
        return res