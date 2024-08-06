class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        prev = [0] * n
        curr = [0] * n
        pref = [float('-inf')] * n
        suff = [float('-inf')] * n
        for i in range(m):
            for j in range(n):
                curr[j] = max(curr[j], pref[j] - j + points[i][j] if i > 0 else points[i][j])
                curr[j] = max(curr[j], suff[j] + j + points[i][j] if i > 0 else points[i][j])
            prev, curr = curr, prev
            for j in range(n):
                pref[j] = max(prev[j] + j, pref[j - 1] if j > 0 else float('-inf'))
            for j in range(n - 1, -1, -1):
                suff[j] = max(prev[j] - j, suff[j + 1] if j + 1 < n else float('-inf'))
        return max(prev)