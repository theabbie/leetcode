class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([el for el in details if int(el[11:13]) > 60])