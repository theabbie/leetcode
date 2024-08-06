class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums.reverse()
        a = []
        b = []
        a.append(nums.pop())
        b.append(nums.pop())
        while len(nums) > 0:
            val = nums.pop()
            if a[-1] > b[-1]:
                a.append(val)
            else:
                b.append(val)
        return a + b