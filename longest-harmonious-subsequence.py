class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        pos = {}
        for i, num in enumerate(nums):
            if num in pos:
                pos[num][1] = i
            else:
                pos[num] = [i, i]
        mlen = 0
        for num in pos:
            if num + 1 in pos:
                mlen = max(mlen, pos[num + 1][1] - pos[num][0] + 1)
        return mlen