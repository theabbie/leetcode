class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))
        vals = [v for v, _ in arr]
        pos = [0] * n
        for i, (_, j) in enumerate(arr):
            pos[j] = i

        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1] + (vals[i] - vals[i - 1] > maxDiff)

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j < n and vals[j] <= vals[i] + maxDiff:
                j += 1
            nxt[i] = j - 1

        logn = (n - 1).bit_length()
        jump = [nxt]
        for k in range(1, logn):
            pre = jump[k - 1]
            cur = [0] * n
            for i in range(n):
                cur[i] = pre[pre[i]]
            jump.append(cur)

        out = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if comp[pu] != comp[pv]:
                out.append(-1)
            elif pu == pv:
                out.append(0)
            else:
                if pu > pv:
                    pu, pv = pv, pu
                x = pu
                ans = 0
                for k in range(logn - 1, -1, -1):
                    y = jump[k][x]
                    if y < pv:
                        x = y
                        ans |= 1 << k
                out.append(ans + 1)
        return out