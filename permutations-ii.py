class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ctr = {}
        for num in nums:
            ctr[num] = ctr.get(num, 0) + 1
        nums = set(nums)
        paths = [([num], { **ctr, num: ctr[num] - 1 }, 1) for num in nums]
        while paths[0][2] < n:
            curr, currCtr, l = paths.pop(0)
            for num in nums:
                if currCtr[num] > 0:
                    paths.append((curr + [num], { **currCtr, num: currCtr[num] - 1 }, l + 1))
        return [perm[0] for perm in paths]