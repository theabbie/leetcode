class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n = len(packages)
        packages.sort()
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + packages[i]
        for box in boxes:
            box.sort()
        res = float('inf')
        for box in boxes:
            choosen = 0
            cost = 0
            for b in box:
                beg = 1
                end = n - choosen
                while beg <= end:
                    mid = (beg + end) // 2
                    if packages[choosen + mid - 1] <= b:
                        beg = mid + 1
                    else:
                        end = mid - 1
                cost += b * (beg - 1) - (p[choosen + beg - 1] - p[choosen])
                choosen += beg - 1
            if choosen != n:
                cost = float('inf')
            res = min(res, cost)
        if res == float('inf'):
            res = -1
        else:
            res %= 10 ** 9 + 7
        return res