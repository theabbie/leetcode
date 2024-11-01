MAX = 1 + 10 ** 6

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.reverse()
        res = 0
        for i in range(1, len(nums)):
            while nums[i] > nums[i - 1]:
                if nums[i] == sp[nums[i]]:
                    return -1
                nums[i] = sp[nums[i]]
                res += 1
        return res