class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        vals = []
        for i, el in enumerate(nums):
            if el & 1:
                vals.append((el, i))
                vals.append((el * 2, i))
            else:
                while el % 2 == 0:
                    vals.append((el, i))
                    el //= 2
                vals.append((el, i))
        vals.sort()
        res = float('inf')
        ctr = [0] * n
        dctr = 0
        i = 0
        for j in range(len(vals)):
            ctr[vals[j][1]] += 1
            if ctr[vals[j][1]] == 1:
                dctr += 1
            while i < j and dctr - int(ctr[vals[i][1]] == 1) >= n:
                ctr[vals[i][1]] -= 1
                if ctr[vals[i][1]] == 0:
                    dctr -= 1
                i += 1
            if dctr >= n:
                res = min(res, vals[j][0] - vals[i][0])
        return res