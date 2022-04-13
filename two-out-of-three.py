class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        checklist = set.union(nums1, nums2, nums3)
        op = []
        for num in checklist:
            ctr = 0
            if num in nums1:
                ctr += 1
            if num in nums2:
                ctr += 1
            if num in nums3:
                ctr += 1
            if ctr >= 2:
                op.append(num)
        return op