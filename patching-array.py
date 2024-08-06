class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        while True:
            nums.sort()
            found = 0
            if nums[0] > 1:
                found = 1
            else:
                p = 0
                for i in range(len(nums)):
                    p += nums[i]
                    if i == len(nums) - 1 or p + 1 < nums[i + 1]:
                        found = p + 1
                        break
            if found > n:
                break
            nums.append(found)
            res += 1
        return res