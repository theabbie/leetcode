from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.ctr = Counter(nums2)
        self.nums2 = nums2
        self.nums1 = nums1

    def add(self, index: int, val: int) -> None:
        self.ctr[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.ctr[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for el in self.nums1:
            res += self.ctr[tot - el]
        return res