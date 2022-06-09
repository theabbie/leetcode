class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i <= j:
            curr = numbers[i] + numbers[j]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return [i + 1, j + 1]
                