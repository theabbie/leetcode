class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        def graph(i):
            l = i - 1
            lmax = float('-inf')
            while l >= 0 and i - l <= d:
                lmax = max(lmax, arr[l])
                if arr[i] > lmax:
                    yield l
                l -= 1
            r = i + 1
            rmax = float('-inf')
            while r < n and r - i <= d:
                rmax = max(rmax, arr[r])
                if arr[i] > rmax:
                    yield r
                r += 1
        dp = [1] * n
        def DFS(i, v):
            for j in graph(i):
                if j not in v:
                    v.add(j)
                    DFS(j, v)
                dp[i] = max(dp[i], 1 + dp[j])
        v = set()
        for i in range(n):
            if i not in v:
                v.add(i)
                DFS(i, v)
        return max(dp)