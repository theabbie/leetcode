class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valIndex = {}
        for i, num in enumerate(nums):
            if num in valIndex:
                curr = valIndex[num][-1]
                if i - curr <= k:
                    return True
                valIndex[num].append(i)
            else:
                valIndex[num] = [i]
        return False