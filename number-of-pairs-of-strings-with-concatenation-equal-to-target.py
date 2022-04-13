from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        k = len(target)
        nums = Counter(nums)
        ctr = 0
        for num in nums:
            if target.startswith(num):
                chunk = target[len(num) - k:]
                if chunk in nums:
                    ctr += nums[num] * nums[chunk]
                    if num == chunk:
                        ctr -= nums[chunk]
        return ctr