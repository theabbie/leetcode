class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.insert(0, 0)
        nums.append(float('inf'))
        print(nums)
        total = 0
        n = len(nums)
        for i in range(n - 1):
            if k >= nums[i + 1] - nums[i] - 1:
                if nums[i + 1] - nums[i] > 1:
                    total += nums[i + 1] * (nums[i + 1] - 1) // 2
                    total -= nums[i] * (nums[i] + 1) // 2
                    k -= nums[i + 1] - nums[i] - 1
            else:
                end = nums[i] + k
                beg = nums[i]
                total += end * (end + 1) // 2
                total -= beg * (beg + 1) // 2
                break
        return total