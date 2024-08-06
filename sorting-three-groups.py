class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lis = []
        for i, el in enumerate(nums):
            el = (el, i)
            pos = bisect_left(lis, el)
            if pos < len(lis):
                lis[pos] = el
            else:
                lis.append(el)
        return len(nums) - len(lis)