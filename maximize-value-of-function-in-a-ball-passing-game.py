class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        LOG = len("{:0b}".format(k)) + 1
        parent = [[-1] * LOG for _ in range(n)]
        val = [[0] * LOG for _ in range(n)]
        for i in range(n):
            parent[i][0] = receiver[i]
            val[i][0] = receiver[i]
        for d in range(1, LOG):
            for i in range(n):
                parent[i][d] = parent[parent[i][d - 1]][d - 1]
                val[i][d] = val[i][d - 1] + val[parent[i][d - 1]][d - 1]
        res = 0
        for i in range(n):
            curr = k
            p = 0
            currval = 0
            currnode = i
            while curr:
                if curr & 1:
                    currval += val[currnode][p]
                    currnode = parent[currnode][p]
                curr //= 2
                p += 1
                res = max(res, currval + i)
        return res