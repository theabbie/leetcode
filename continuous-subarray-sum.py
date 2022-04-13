class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ctr = 0
        total = [ctr]
        for num in nums:
            ctr += num
            total.append(ctr)
        exists = {}
        for i, f in enumerate(total):
            rem = f % k
            if rem in exists:
                if i - exists[rem] >= 2:
                    return True
            else:
                exists[rem] = i
        return False