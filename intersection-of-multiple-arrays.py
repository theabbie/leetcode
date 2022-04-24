class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(set.intersection(*[set(num) for num in nums]))