class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]
        for i in range(rowIndex):
            curr = [0] + curr + [0]
            n = len(curr)
            for i in range(n - 1):
                curr[i] = curr[i] + curr[i + 1]
            curr.pop()
        return curr