class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        op = []
        for i in range(left, right + 1):
            curr = i
            valid = True
            while curr != 0:
                d = curr % 10
                if d == 0 or i % d != 0:
                    valid = False
                    break
                curr //= 10
            if valid:
                op.append(i)
        return op