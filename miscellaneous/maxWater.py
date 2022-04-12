def maxArea(height):
        n = len(height)
        mvol = 0
        indexes = {}
        for h in range(n):
            indexes[height[h]] = indexes.get(height[h], []) + [h]
        dist_heights = sorted(indexes.keys())
        nn = len(dist_heights)
        for h in range(nn):
            for mind in indexes[dist_heights[h]]:
                mdist = 0
                if dist_heights[h] * max(mind, n - 1 - mind) <= mvol:
                    continue
                for hh in dist_heights[h:]:
                    for i in indexes[hh]:
                        cdist = abs(i - mind)
                        if cdist > mdist:
                            mdist = cdist
                    mvol = max(mvol, dist_heights[h] * mdist)
        return mvol

print(maxArea([8,10,14,0,13,10,9,9,11,11]))