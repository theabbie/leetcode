class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        ctr = {}
        for num in nums:
            ctr[num] = ctr.get(num, 0) + 1
        return [num for num, count in ctr.items() if count > k]