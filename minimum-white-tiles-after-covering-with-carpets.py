class Solution:
    def minTiles(self, floor: str, numCarpets: int, carpetLen: int, i, n) -> int:
        key = (i, numCarpets)
        if i >= n:
            return 0
        if key in self.cache:
            return self.cache[key]
        if numCarpets <= 0:
            val = floor[i:].count("1")
            self.cache[key] = val
            return val
        a = float('inf')
        if floor[i] == "1":
            a = self.minTiles(floor, numCarpets - 1, carpetLen, i + carpetLen, n)
        b = self.minTiles(floor, numCarpets, carpetLen, i + 1, n)
        if floor[i] == "1":
            b += 1
        val = min(a, b)
        self.cache[key] = val
        return val
    
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int, i = 0) -> int:
        self.cache = {}
        return self.minTiles(floor, numCarpets, carpetLen, 0, len(floor))