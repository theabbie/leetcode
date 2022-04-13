class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        exist = {}
        for i, num in enumerate(numbers):
            if (target - num) in exist:
                return [exist[target - num], i + 1]
            exist[num] = i + 1
                