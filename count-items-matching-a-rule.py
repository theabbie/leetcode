class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        ctr = 0
        for item in items:
            if ruleValue == item[index[ruleKey]]:
                ctr += 1
        return ctr