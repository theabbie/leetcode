class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ctr = set()
        for num in nums:
            ctr.add(num)
            curr = 0
            while num:
                curr = 10 * curr + num % 10
                num //= 10
            ctr.add(curr)
        return len(ctr)