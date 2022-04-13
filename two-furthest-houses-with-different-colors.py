class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        indexes = {}
        for i, c in enumerate(colors):
            if c in indexes:
                indexes[c] = (min(i, indexes[c][0]), max(i, indexes[c][1]))
            else:
                indexes[c] = (i, i)
        mdiff = 1
        n = len(indexes)
        colors = list(indexes.keys())
        for i in range(n):
            for j in range(i + 1, n):
                mdiff = max(mdiff, abs(indexes[colors[i]][1] - indexes[colors[j]][0]), abs(indexes[colors[j]][1] - indexes[colors[i]][0]))
        return mdiff