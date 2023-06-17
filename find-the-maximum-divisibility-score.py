class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        n = len(divisors)
        ctr = [0] * n
        for i in range(n):
            for el in nums:
                if el % divisors[i] == 0:
                    ctr[i] += 1
        return divisors[max(range(n), key = lambda x: (ctr[x], -divisors[x]))]