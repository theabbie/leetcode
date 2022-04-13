class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = 0
        freq = [0]
        maxLen = 0
        for num in nums:
            if num == 1:
                ctr += 1
            else:
                ctr -= 1
            freq.append(ctr)
        exists = {}
        for i, f in enumerate(freq):
            if f in exists:
                maxLen = max(maxLen, i - exists[f])
            else:
                exists[f] = i
        return maxLen