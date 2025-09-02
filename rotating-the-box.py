class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [["."] * m for _ in range(n)]
        for i in range(m):
            ctr = 0
            for j in range(n):
                if box[i][j] == "#":
                    ctr += 1
                elif box[i][j] == "*":
                    res[j][m - i - 1] = "*"
                if j == n - 1 or box[i][j + 1] == "*":
                    for x in range(ctr):
                        res[j - x][m - i - 1] = "#"
                    ctr = 0
        return res