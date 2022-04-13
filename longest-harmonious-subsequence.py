class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        pos = {}
        mlen = 0
        for i, num in enumerate(nums):
            pos[num] = pos.get(num, []) + [i]
        for num in pos:
            if num + 1 in pos:
                mlen = max(mlen, max(pos[num + 1]) - min(pos[num]) + 1)
        return mlen