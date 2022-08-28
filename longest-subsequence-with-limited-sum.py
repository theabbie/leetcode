import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        res = []
        for m in queries:
            j = bisect.bisect_left(p, m)
            if j < len(p) and p[j] == m:
                res.append(j)
            else:
                res.append(j - 1)
        return res