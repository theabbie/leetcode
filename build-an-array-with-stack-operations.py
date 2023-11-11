class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        for j in range(1, target[-1] + 1):
            while i < len(target) and target[i] < j:
                i += 1
            res.append("Push")
            if i == len(target) or target[i] != j:
                res.append("Pop")
        return res