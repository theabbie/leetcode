# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         k = len(nums) // 3
#         ctr = {}
#         for num in nums:
#             ctr[num] = ctr.get(num, 0) + 1
#         return [num for num, count in ctr.items() if count > k]
    
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