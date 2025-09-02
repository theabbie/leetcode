class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        ctr = Counter()
        res = 0
        for x2, y2 in coordinates:
            for l in range(k + 1):
                x1 = x2 ^ l
                y1 = y2 ^ (k - l)
                res += ctr[(x1, y1)]
            ctr[(x2, y2)] += 1
        return res