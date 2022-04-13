class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        curr = [1]
        for i in range(numRows):
            tri.append(curr)
            curr = [0] + curr + [0]
            n = len(curr)
            for i in range(n - 1):
                curr[i] = curr[i] + curr[i + 1]
            curr.pop()
        return tri