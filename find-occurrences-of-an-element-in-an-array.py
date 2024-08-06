class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = []
        for i in range(len(nums)):
            if nums[i] == x:
                pos.append(i)
        return [pos[q - 1] if q <= len(pos) else -1 for q in queries]