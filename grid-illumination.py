from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rowctr = Counter()
        colctr = Counter()
        posdiagctr = Counter()
        negdiagctr = Counter()
        onlamps = set()
        for i, j in lamps:
            if (i, j) not in onlamps:
                rowctr[i] += 1
                colctr[j] += 1
                posdiagctr[i + j] += 1
                negdiagctr[i - j] += 1
                onlamps.add((i, j))
        res = []
        for i, j in queries:
            if rowctr[i] > 0 or colctr[j] > 0 or posdiagctr[i + j] > 0 or negdiagctr[i - j] > 0:
                res.append(1)
            else:
                res.append(0)
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < n and 0 <= y < n and (x, y) in onlamps:
                        onlamps.remove((x, y))
                        rowctr[x] -= 1
                        colctr[y] -= 1
                        posdiagctr[x + y] -= 1
                        negdiagctr[x - y] -= 1
        return res