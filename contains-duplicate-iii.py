import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        indices = {}
        for i, el in enumerate(nums):
            if el in indices:
                indices[el].append(i)
            else:
                indices[el] = [i]
        vals = sorted(indices.keys())
        n = len(vals)
        for i in range(n):
            j = i
            while j < n and vals[j] - vals[i] <= t:
                for a in indices[vals[i]]:
                    b = bisect.bisect_right(indices[vals[j]], a)
                    b = min(b, len(indices[vals[j]]) - 1)
                    bi = indices[vals[j]][b - 1]
                    bj = indices[vals[j]][b]
                    if 0 < abs(a - bj) <= k or 0 < abs(a - bi) <= k:
                        return True
                j += 1
        return False