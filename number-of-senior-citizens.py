class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for el in details:
            if int(el[11:13]) > 60:
                res += 1
        return res