class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        indices = {}
        for i, el in enumerate(nums):
            indices[el] = indices.get(el, []) + [i]
        vals = sorted(indices.keys())
        n = len(vals)
        for i in range(n):
            j = i
            while j < n and vals[j] - vals[i] <= t:
                for a in indices[vals[i]]:
                    for b in indices[vals[j]]:
                        if a != b:
                            if abs(a - b) <= k:
                                return True
                j += 1
        return False