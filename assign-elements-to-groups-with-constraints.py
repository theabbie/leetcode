class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        M = max(groups)
        f = [-1] * (M + 1)
        seen = set()
        for j in range(len(elements)):
            if elements[j] in seen:
                continue
            seen.add(elements[j])
            mul = 1
            while elements[j] * mul <= M:
                if f[elements[j] * mul] == -1:
                    f[elements[j] * mul] = j
                mul += 1
        return [f[x] for x in groups]