class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        averages = {}
        groups = {}
        for i in range(m - 2):
            for j in range(n - 2):
                valid = True
                s = 0
                for x in range(3):
                    for y in range(3):
                        s += image[i + x][j + y]
                        if x > 0 and abs(image[i + x - 1][j + y] - image[i + x][j + y]) > threshold:
                            valid = False
                            break
                        if y > 0 and abs(image[i + x][j + y - 1] - image[i + x][j + y]) > threshold:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    for x in range(3):
                        for y in range(3):
                            if (i + x, j + y) not in groups:
                                groups[(i + x, j + y)] = []
                            groups[(i + x, j + y)].append(s // 9)
        for i in range(m):
            for j in range(n):
                if (i, j) in groups:
                    image[i][j] = sum(groups[(i, j)]) // len(groups[(i, j)])
        return image