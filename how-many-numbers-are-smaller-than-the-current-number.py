class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for num in nums]
        order = sorted([(num, i) for i, num in enumerate(nums)])
        for i in range(n):
            ans[order[i][1]] = len([order[k][0] for k in range(i) if order[k][0] != order[i][0]])
        return ans