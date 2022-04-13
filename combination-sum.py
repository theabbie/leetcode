class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        op = set()
        combs = [[item] for item in candidates]
        while len(combs) > 0:
            comb = combs.pop(0)
            currsum = sum(comb)
            if sum(comb) == target:
                op.add(tuple(sorted(comb)))
            for item in candidates:
                if currsum + item <= target:
                    combs.append(comb + [item])
        return [list(item) for item in op]
        