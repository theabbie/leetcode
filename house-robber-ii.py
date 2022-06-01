class Solution:
    def robRec(self, nums, i, n, beg, isFirstRobbed):
        if i >= n + beg:
            return 0
        if i == n + beg - 1:
            if isFirstRobbed:
                return 0
            return nums[i % n]
        if (i, isFirstRobbed) in self.cache:
            return self.cache[(i, isFirstRobbed)]
        maxRob = nums[i % n]
        for j in range(i + 2, beg + n):
            maxRob = max(maxRob, nums[i % n] + self.robRec(nums, j, n, beg, isFirstRobbed))
        self.cache[(i, isFirstRobbed)] = maxRob
        return maxRob
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        self.cache = {}
        maxRob = 0
        for i in range(n):
            maxRob = max(maxRob, self.robRec(nums, i, n, i, True), self.robRec(nums, i + 1, n, i, False))
        return maxRob