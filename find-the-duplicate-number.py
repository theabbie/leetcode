class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()
        for num in nums:
            if num in dup:
                return num
            dup.add(num)