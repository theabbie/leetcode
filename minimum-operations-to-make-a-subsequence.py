class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        res = []
        pos = {}
        for i in range(len(target)):
            pos[target[i]] = i
        for el in arr:
            if el not in pos:
                continue
            x = bisect.bisect_left(res, pos[el])
            if x < len(res):
                res[x] = pos[el]
            else:
                res.append(pos[el])
        return len(target) - len(res)