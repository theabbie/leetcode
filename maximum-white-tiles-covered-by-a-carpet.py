class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        n = len(tiles)
        tiles.sort()
        tiles.append((float('inf'), float('inf')))
        res = s = 0
        j = -1
        for i in range(n):
            while j + 1 < n and tiles[j + 1][1] <= tiles[i][0] + carpetLen - 1:
                j += 1
                s += tiles[j][1] - tiles[j][0] + 1
            res = max(res, s + max(tiles[i][0] + carpetLen - tiles[j + 1][0], 0))
            s -= tiles[i][1] - tiles[i][0] + 1
        return res