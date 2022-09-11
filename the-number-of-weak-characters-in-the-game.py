class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        seq = sorted(range(n), key = lambda i: properties[i][0])
        res = 0
        mval = float('-inf')
        currmval = float('-inf')
        for i in range(n - 1, -1, -1):
            if i < n - 1 and properties[seq[i]][0] < properties[seq[i + 1]][0]:
                mval = currmval
            if properties[seq[i]][1] < mval:
                res += 1
            currmval = max(currmval, properties[seq[i]][1])
        return res