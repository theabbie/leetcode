class Solution:
    def isSorted(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for i, c in enumerate(order):
            pos[c] = i
        return self.isSorted([tuple([pos.get(c, 0) for c in word]) for word in words])