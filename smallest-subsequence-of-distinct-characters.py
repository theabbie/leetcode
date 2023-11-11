from collections import defaultdict

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        pos = defaultdict(list)
        for i in range(n):
            pos[s[i]].append(i)
        prev = -1
        res = []
        rem = set(s)
        k = len(rem)
        for _ in range(k):
            for cc in sorted(rem):
                beg = 0
                end = len(pos[cc]) - 1
                curr = n
                while beg <= end:
                    mid = (beg + end) // 2
                    if pos[cc][mid] > prev:
                        curr = pos[cc][mid]
                        end = mid - 1
                    else:
                        beg = mid + 1
                if curr < n:
                    if all(pos[ccc][-1] > curr for ccc in rem if ccc != cc):
                        res.append(cc)
                        rem.remove(cc)
                        prev = curr
                        break
        return "".join(res)