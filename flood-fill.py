class Solution:
    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, og) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        if image[sr][sc] == color:
            return
        image[sr][sc] = color
        for x, y in [(sr - 1, sc), (sr, sc - 1), (sr + 1, sc), (sr, sc + 1)]:
            if 0 <= x < m and 0 <= y < n and image[x][y] == og:
                self.fill(image, x, y, color, og)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.fill(image, sr, sc, color, image[sr][sc])
        return image