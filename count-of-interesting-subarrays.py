class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        p = [0]
        for el in nums:
            p.append(p[-1] + int((el % modulo) == k))
        res = 0
        ctr = Counter()
        for el in p:
            res += ctr[(el - k) % modulo]
            ctr[el % modulo] += 1
        return res