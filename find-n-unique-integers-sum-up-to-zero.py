class Solution:
    def sumZero(self, n: int) -> List[int]:
        op = []
        if n % 2 == 0:
            for i in range(1, 1 + (n // 2)):
                op.append(i)
                op.append(-i)
        else:
            op.append(0)
            for i in range(1, 1 + (n - 1) // 2):
                op.append(i)
                op.append(-i)
        return op