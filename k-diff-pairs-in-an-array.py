class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        exists = {}
        ctr = set()
        for i, num in enumerate(nums):
            exists[num] = exists.get(num, []) + [i]
        for i, num in enumerate(nums):
            for val in [num - k, num + k]:
                if val in exists:
                    for j in exists[val]:
                        if j > i:
                            ctr.add(tuple(sorted([nums[i], nums[j]])))
        return len(ctr)