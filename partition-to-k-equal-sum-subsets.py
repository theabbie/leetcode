class Solution:
    def isPossible(self, i, sides, k, nums, n, total):
        if i >= n:
            return len(set(sides)) == 1
        key = tuple(sorted(sides) + [i])
        if key in self.cache:
            return self.cache[key]
        for j in range(k):
            if k * (sides[j] + nums[i]) > total:
                continue
            sides[j] += nums[i]
            curr = self.isPossible(i + 1, sides, k, nums, n, total)
            if curr:
                self.cache[key] = True
                return True
            else:
                sides[j] -= nums[i]
        self.cache[key] = False
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        nums.sort(reverse = True)
        self.cache = {}
        return self.isPossible(0, [0] * k, k, nums, n, total)