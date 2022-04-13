class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valIndex = {}
        for i, num in enumerate(nums):
            valIndex[num] = valIndex.get(num, []) + [i]
        for val in valIndex.values():
            for i, v in enumerate(val):
                if i > 0:
                    if v - val[i - 1] <= k:
                        return True
        return False