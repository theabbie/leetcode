class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = set()
        for i, el in enumerate(nums):
            if el == key:
                for j in range(max(i - k, 0), min(i + k + 1, n)):
                    indices.add(j)
        return sorted(indices)