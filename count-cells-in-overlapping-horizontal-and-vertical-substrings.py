class Solution:
    def countCells(self, grid, pattern):
        n, m = len(grid), len(grid[0])
        s1 = ''.join(''.join(row) for row in grid)
        tmp = []
        for c in range(m):
            for r in range(n):
                tmp.append(grid[r][c])
        s2 = ''.join(tmp)
        k = len(pattern)
        lps = [0] * k
        j = 0
        for i in range(1, k):
            while j and pattern[i] != pattern[j]:
                j = lps[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        def find(text):
            res = []
            j = 0
            for i, ch in enumerate(text):
                while j and ch != pattern[j]:
                    j = lps[j-1]
                if ch == pattern[j]:
                    j += 1
                    if j == k:
                        res.append(i - k + 1)
                        j = lps[j-1]
            return res
        total = n * m
        rd = [0] * (total + 1)
        cd = [0] * (total + 1)
        for p in find(s1):
            rd[p] += 1
            rd[p+k] -= 1
        for p in find(s2):
            cd[p] += 1
            cd[p+k] -= 1
        rm = [0] * total
        cm = [0] * total
        acc = 0
        for i in range(total):
            acc += rd[i]
            if acc:
                rm[i] = 1
        acc = 0
        for i in range(total):
            acc += cd[i]
            if acc:
                cm[i] = 1
        ans = 0
        for r in range(n):
            for c in range(m):
                if rm[r*m + c] and cm[c*n + r]:
                    ans += 1
        return ans