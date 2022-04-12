class Solution:
    def findIntegers(self, n: int) -> int:
        ctr = 1
        nums = ['1']
        maxBits = len("{0:b}".format(n))
        while len(nums) > 0:
            curr = nums.pop(0)
            if int(curr, 2) <= n:
                ctr += 1
                if len(curr) < maxBits:
                    nums.append(curr + '0')
                    if curr[-1] != '1':
                        nums.append(curr + '1')
        return ctr


print(Solution().findIntegers(10000000))