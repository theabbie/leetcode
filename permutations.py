class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        paths = [([num], {num}, 1) for num in nums]
        while paths[0][2] < n:
            curr, currSet, l = paths.pop(0)
            for num in nums:
                if num not in currSet:
                    paths.append((curr + [num], currSet.union({num}), l + 1))
        return [perm[0] for perm in paths]