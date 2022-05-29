class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n - 2):
                b = nums[j]
                start = j + 1
                end = n - 1
                while start < end:
                    c = nums[start]
                    d = nums[end]
                    total = b + c + d
                    if total == target - a:
                        res.add(tuple([a, b, c, d]))
                        start += 1
                        end -= 1
                    elif total > target - a:
                        end -= 1
                    else:
                        start += 1
        return list(res)