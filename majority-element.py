class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = {}
        for num in nums:
            ctr[num] = ctr.get(num, 0) + 1
        return max([(v, k) for k, v in ctr.items()])[1]