import bisect

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for h in range(n, -1, -1):
            if h <= n - bisect.bisect_left(citations, h):
                return h