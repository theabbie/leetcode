from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(list)
        for el in nums:
            curr = sum(int(d) for d in str(el))
            sums[curr].append(el)
        msum = -1
        for el in sums:
            if len(sums[el]) > 1:
                currmax = sorted(sums[el])
                msum = max(msum, currmax[-1] + currmax[-2])
        return msum