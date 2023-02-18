class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [nums[0]]
        for i in range(1, n):
            currval = nums[i]
            while len(stack) > 0 and self.gcd(stack[-1], currval) > 1:
                prev = stack.pop()
                currval = prev * currval // self.gcd(prev, currval)
            stack.append(currval)
        return stack