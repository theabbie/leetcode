class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ctr = 0
        total = [ctr]
        for num in nums:
            ctr = (ctr + num) % k
            total.append(ctr)
        exists = {}
        for i, f in enumerate(total):
            if f in exists:
                if i - exists[f] >= 2:
                    return True
            else:
                exists[f] = i
        return False