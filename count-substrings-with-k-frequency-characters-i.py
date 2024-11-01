class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        p = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for c in range(26):
                p[i + 1][c] = p[i][c] + int(c == ord(s[i]) - ord('a'))
        res = 0
        for i in range(n):
            beg = i
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                good = False
                for c in range(26):
                    if p[mid + 1][c] - p[i][c] >= k:
                        good = True
                        break
                if good:
                    end = mid - 1
                else:
                    beg = mid + 1
            res += n - end - 1
        return res