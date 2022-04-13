import math

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for j in range(math.ceil(n/2)):
            for i in range(n):
                image[i][j], image[i][n - j - 1] = 1 - image[i][n - j - 1], 1 - image[i][j]
        return image