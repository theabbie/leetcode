class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        num = list(num)
        x = 0
        while x < n and change[int(num[x])] <= int(num[x]):
            x += 1
        while x < n and change[int(num[x])] >= int(num[x]):
            num[x] = str(change[int(num[x])])
            x += 1
        return "".join(num)