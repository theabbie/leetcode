class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {0:-1}
        curr = 0
        mlen = 0
        for i in range(n):
            curr += 2 * nums[i] - 1
            if curr in seen:
                mlen = max(mlen, i - seen[curr])
            else:
                seen[curr] = i
        return mlen