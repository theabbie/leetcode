class Solution:
    def ff(self, image: List[List[int]], i, j, newColor: int, currColor, visited) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        if i >= 0 and j >= 0 and i < m and j < n and image[i][j] == currColor and (i, j) not in visited:
            image[i][j] = newColor
            visited.add((i, j))
            self.ff(image, i - 1, j, newColor, currColor, visited)
            self.ff(image, i + 1, j, newColor, currColor, visited)
            self.ff(image, i, j - 1, newColor, currColor, visited)
            self.ff(image, i, j + 1, newColor, currColor, visited)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, currColor = None) -> List[List[int]]:
        currColor = image[sr][sc]
        self.ff(image, sr, sc, newColor, currColor, set())
        return image