class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        chunks = []
        i = 0
        zeroFound = False
        mlen = 0
        msingle = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            chunks.append((nums[i - 1], ctr))
            if nums[i - 1] == 1:
                msingle = max(msingle, ctr)
            else:
                zeroFound = True
        k = len(chunks)
        for i in range(1, k - 1):
            if chunks[i] == (0, 1):
                mlen = max(mlen, chunks[i - 1][1] + chunks[i + 1][1])
        if zeroFound:
            mlen = max(mlen, msingle)
        else:
            mlen = max(mlen, msingle - 1)
        return mlen