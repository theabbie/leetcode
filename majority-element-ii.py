class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        elms = set(nums)
        op = []
        for x in elms:
            ctr = bisect.bisect_right(nums, x) - bisect.bisect_left(nums, x)
            if ctr > n // 3:
                op.append(x)
        return op