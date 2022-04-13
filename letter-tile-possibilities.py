class Solution:
    def numTiles(self, tiles, ctr):
        num = 0
        for c in ctr:
            if ctr[c] > 0:
                num += 1
                num += self.numTiles(tiles + c, {**ctr, c: ctr[c] - 1})
        return num
    
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        ctr = {}
        for c in tiles:
            ctr[c] = ctr.get(c, 0) + 1
        return self.numTiles("", ctr)