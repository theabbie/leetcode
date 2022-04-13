class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ctr = 0
        i = 2
        while i < n:
            a = 0
            b = i - 1
            while a < b:
                if nums[a] + nums[b] > nums[i]:
                    ctr += (b - a)
                    b -= 1
                else:
                    a += 1
            i += 1
        return ctr