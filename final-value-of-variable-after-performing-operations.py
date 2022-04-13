class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if o[1] == '+':
                x += 1
            if o[1] == '-':
                x -= 1
        return x