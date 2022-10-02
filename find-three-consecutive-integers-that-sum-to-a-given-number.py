class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            k = num // 3
            return [k - 1, k, k + 1]
        return []