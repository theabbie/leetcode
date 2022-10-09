class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res = 0
        i = 0
        while i < n:
            ctr = 1
            mtime = total = neededTime[i]
            while i < n - 1 and colors[i] == colors[i + 1]:
                i += 1
                ctr += 1
                mtime = max(mtime, neededTime[i])
                total += neededTime[i]
            i += 1
            if ctr > 1:
                res += total - mtime
        return res