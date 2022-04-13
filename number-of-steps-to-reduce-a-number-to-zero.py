class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1:
                num = (num - 1) // 2
                steps += 1 if num == 0 else 2
            else:
                num = num // 2
                steps += 1
        return steps