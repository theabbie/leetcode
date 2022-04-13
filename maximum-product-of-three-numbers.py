class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[2], nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# import heapq

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums = [(-abs(n), 1 if n >= 0 else -1) for n in nums]
#         heapq.heapify(nums)
#         s = 1
#         p = 1
#         for i in range(3):
#             curr, sign = heapq.heappop(nums)
#             curr *= -1
#             while curr == 0:
#                 if len(nums) > 0:
#                     curr, sign = heapq.heappop(nums)
#                 else:
#                     return 0
#             p *= curr
#             s *= sign
#         return p * sign