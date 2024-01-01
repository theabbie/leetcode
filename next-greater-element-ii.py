class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        B = int(pow(2 * n, 0.5) + 1)
        maxes = [float('-inf')] * B
        for i in range(2 * n):
            maxes[i // B] = max(maxes[i // B], nums[i % n])
        res = [-1] * n
        for i in range(n):
            j = i + 1
            while j < 2 * n:
                if nums[j % n] > nums[i]:
                    res[i] = nums[j % n]
                    break
                if j % B == 0 and j + B <= 2 * n and maxes[j // B] <= nums[i]:
                    j += B
                else:
                    j += 1
        return res