class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        exists = set()
        op = []
        for num in nums:
            if num in exists:
                op.append(num)
            else:
                exists.add(num)
        return op