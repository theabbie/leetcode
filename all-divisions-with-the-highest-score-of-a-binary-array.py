class Solution:
    def maxScoreIndices(self, nums):
        rightones = nums.count(1)
        leftzeroes = 0
        mscore = leftzeroes + rightones
        res = [0]
        for i, el in enumerate(nums):
            if el == 0:
                leftzeroes += 1
            else:
                rightones -= 1
            if leftzeroes + rightones > mscore:
                mscore = leftzeroes + rightones
                res = [i + 1]
            elif mscore == leftzeroes + rightones:
                res.append(i + 1)
        return res