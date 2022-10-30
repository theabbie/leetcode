class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        nums.sort()
        target.sort()
        evens = [el for el in nums if not el & 1]
        tevens = [el for el in target if not el & 1]
        odds = [el for el in nums if el & 1]
        todds = [el for el in target if el & 1]
        p = len(evens)
        q = len(odds)
        res = 0
        for i in range(p):
            res += abs(evens[i] - tevens[i]) // 2
        for i in range(q):
            res += abs(odds[i] - todds[i]) // 2
        return res // 2