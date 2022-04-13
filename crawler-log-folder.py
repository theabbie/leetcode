class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ctr = 0
        for log in logs:
            if log == "../":
                ctr =  max(ctr - 1, 0)
            elif log != "./":
                ctr += 1
        return ctr