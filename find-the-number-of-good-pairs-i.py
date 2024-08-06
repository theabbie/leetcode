class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        M = max(nums1)
        res = 0
        fctr = Counter(nums1)
        ctr = Counter(nums2)
        for el in ctr:
            mul = 1
            while el * k * mul <= M:
                res += ctr[el] * fctr[el * k * mul]
                mul += 1
        return res