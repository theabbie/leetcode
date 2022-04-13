class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        exists = {}
        ctr = 0
        for i, num in enumerate(nums):
            exists[num] = exists.get(num, []) + [i]
        for i, num in enumerate(nums):
            for val in [num - k, num + k]:
                if val in exists:
                    for j in exists[val]:
                        if j > i:
                            ctr += 1
        return ctr