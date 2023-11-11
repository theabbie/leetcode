class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        rem = set(range(1, k + 1))
        res = 0
        while len(nums) > 0 and len(rem) > 0:
            curr = nums.pop()
            if curr in rem:
                rem.remove(curr)
            res += 1
        return res