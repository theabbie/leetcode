from functools import cmp_to_key

class Solution:
    def compare(self, a, b):
        if a + b > b + a:
            return -1
        return 1
    
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(sorted([str(num) for num in nums], key = cmp_to_key(self.compare)))))