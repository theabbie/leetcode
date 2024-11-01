from sortedcontainers import SortedList
 
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        M = max(arr)
        dp = [[False, False] for _ in range(n)]
        dp[n - 1][0] = dp[n - 1][1] = True
        vals = SortedList()
        valmap = {}
        res = 0
        for i in range(n - 1, -1, -1):
            odd = even = False
            pos = vals.bisect_left((arr[i], float('-inf')))
            if pos < len(vals):
                odd = vals[pos][1]
            if pos == len(vals) or vals[pos][0] > arr[i]:
                pos -= 1
            if pos >= 0:
                even = vals[pos][1]
            if arr[i] in valmap:
                vals.remove((arr[i], valmap[arr[i]]))
            valmap[arr[i]] = min(valmap.get(arr[i], float('inf')), i)
            vals.add((arr[i], i))
            if odd and dp[odd][0]:
                dp[i][1] = True
            if even and dp[even][1]:
                dp[i][0] = True
            if dp[i][1]:
                res += 1
        return res