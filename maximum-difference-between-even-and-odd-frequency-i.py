class Solution:
    def maxDifference(self, s: str) -> int:
        mn = [float('inf'), float('inf')]
        mx = [float('-inf'), float('-inf')]
        for x in Counter(s).values():
            mn[x % 2] = min(mn[x % 2], x)
            mx[x % 2] = max(mx[x % 2], x)
        return mx[1] - mn[0]