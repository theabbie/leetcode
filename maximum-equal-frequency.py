from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ctr = Counter()
        ctrctr = Counter()
        ctrctr[0] = n
        nzfreq = 0
        for i in range(n):
            ctrctr[ctr[nums[i]]] -= 1
            if ctrctr[ctr[nums[i]]] == 0:
                if ctr[nums[i]] != 0:
                    nzfreq -= 1
                del ctrctr[ctr[nums[i]]]
            ctr[nums[i]] += 1
            ctrctr[ctr[nums[i]]] += 1
            if ctrctr[ctr[nums[i]]] == 1 and ctr[nums[i]] != 0:
                nzfreq += 1
            if nzfreq <= 2:
                for el in ctrctr:
                    if el == 0:
                        continue
                    curr = Counter(ctrctr)
                    curr[el - 1] += 1
                    curr[el] -= 1
                    if len([x for x in curr if x != 0 and curr[x] != 0]) == 1:
                        res = i + 1
                        break
        return res