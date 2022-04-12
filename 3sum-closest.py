class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return []
        nums = [3 * num - target for num in nums]
        nums.sort()
        closest = float('inf')
        for i in range(n - 2):
            a = nums[i]
            start = i + 1
            end = n - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                total = a + b + c
                if abs(total) < abs(closest):
                    closest = total
                if total > 0:
                    end -= 1
                else:
                    start += 1
        return target + closest // 3