class Solution:
    def maximizeWin(self, pos, k):
        n = len(pos)
        l = [0] * n
        r = [0] * n
        i = 0
        for j in range(n):
            while i < j and pos[j] - pos[i] > k:
                i += 1
            if pos[j] - pos[i] <= k:
                l[j] = j - i + 1
        i = n - 1
        for j in range(n - 1, -1, -1):
            while i > j and pos[i] - pos[j] > k:
                i -= 1
            if pos[i] - pos[j] <= k:
                r[j] = i - j + 1
        res = 0
        maxleft = 0
        for i in range(n):
            res = max(res, maxleft + r[i])
            maxleft = max(maxleft, l[i])
        return res