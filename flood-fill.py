class Solution:
    def ff(self, image: List[List[int]], i, j, newColor: int, currColor) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        if i >= 0 and j >= 0 and i < m and j < n and image[i][j] == currColor:
            image[i][j] = newColor
            self.ff(image, i - 1, j, newColor, currColor)
            self.ff(image, i + 1, j, newColor, currColor)
            self.ff(image, i, j - 1, newColor, currColor)
            self.ff(image, i, j + 1, newColor, currColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, currColor = None) -> List[List[int]]:
        currColor = image[sr][sc]
        if currColor != newColor:
            self.ff(image, sr, sc, newColor, currColor)
        return image