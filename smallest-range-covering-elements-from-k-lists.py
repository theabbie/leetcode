from collections import defaultdict, Counter

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        vals = defaultdict(set)
        for i in range(m):
            for el in nums[i]:
                vals[el].add(i)
        vals = sorted(vals.items())
        k = len(vals)
        res = [float('-inf'), float('inf')]
        i = 0
        ctr = Counter()
        for j in range(k):
            for el in vals[j][1]:
                ctr[el] += 1
            beg = i
            while i < j and len(ctr) == m:
                distvals = len(ctr)
                for el in vals[i][1]:
                    if ctr[el] == 1:
                        distvals -= 1
                if len(ctr) == m and distvals < m:
                    break
                if len(ctr) == m and distvals == m:
                    for el in vals[i][1]:
                        ctr[el] -= 1
                        if ctr[el] == 0:
                            del ctr[el]
                i += 1
            if len(ctr) == m and vals[j][0] - vals[i][0] < res[1] - res[0]:
                res = [vals[i][0], vals[j][0]]
        return res