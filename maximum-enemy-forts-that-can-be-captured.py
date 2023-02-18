class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        res = 0
        for i in range(n):
            if forts[i] == 1:
                l = i - 1
                r = i + 1
                while l >= 0 and forts[l] == 0:
                    l -= 1
                while r < n and forts[r] == 0:
                    r += 1
                if l >= 0 and forts[l] == -1:
                    res = max(res, i - l - 1)
                if r < n and forts[r] == -1:
                    res = max(res, r - i - 1)
        return res