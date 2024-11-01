class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        ctr = Counter()
        for i in range(n):
            ctr[nums[i]] += 1
            if i >= k:
                ctr[nums[i - k]] -= 1
                if ctr[nums[i - k]] == 0:
                    del ctr[nums[i - k]]
            if i >= k - 1:
                res.append(len(ctr))
        return res