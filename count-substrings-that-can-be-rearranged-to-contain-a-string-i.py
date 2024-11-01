class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m < n:
            return 0
        pos = lambda c: ord(c) - ord('a')
        p = [[0] * 26 for _ in range(m + 1)]
        for i in range(m):
            for c in range(26):
                p[i + 1][c] = p[i][c]
            p[i + 1][pos(word1[i])] += 1
        tctr = [0] * 26
        for c in word2:
            tctr[pos(c)] += 1
        res = 0
        for i in range(m):
            beg = i
            end = m - 1
            while beg <= end:
                mid = (beg + end) // 2
                good = True
                for c in range(26):
                    if p[mid + 1][c] - p[i][c] < tctr[c]:
                        good = False
                        break
                if good:
                    end = mid - 1
                else:
                    beg = mid + 1
            res += m - end - 1
        return res