class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        paths = [([num], {num}) for num in nums]
        while len(paths[0][0]) < n:
            curr, currSet = paths.pop(0)
            for num in nums:
                if num not in currSet:
                    paths.append((curr + [num], currSet.union({num})))
        return [perm[0] for perm in paths]