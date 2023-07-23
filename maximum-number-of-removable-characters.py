class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        beg = 1
        end = len(removable)
        pos = {}
        for i in range(len(removable)):
            pos[removable[i]] = i
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            i = 0
            for j in range(n):
                if j not in pos or pos[j] >= mid:
                    if i < len(p) and s[j] == p[i]:
                        i += 1
            if i == len(p):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res