class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n
        curr = 0
        pos = {0: -1}
        mlen = 0
        for i in range(n):
            curr += nums[i]
            if (curr - total + x) in pos:
                mlen = max(mlen, i - pos[curr - total + x])
            pos[curr] = i
        if mlen == 0:
            return -1
        return n - mlen