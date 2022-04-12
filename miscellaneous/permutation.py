class Solution:
    def permute(self, nums):
        n = len(nums)
        paths = [([num], {num}, 1) for num in nums]
        while paths[0][2] < n:
            curr, currSet, l = paths.pop(0)
            for num in nums:
                if num not in currSet:
                    paths.append((curr + [num], currSet.union({num}), l + 1))
        return [perm[0] for perm in paths]

print(Solution().permute([1,2,3, 4, 5, 6, 7]))