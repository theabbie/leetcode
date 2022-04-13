class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        op = []
        combs = [([item], item) for item in candidates]
        while len(combs) > 0:
            comb, currsum = combs.pop(0)
            if currsum == target:
                op.append(comb)
            for item in candidates:
                newsum = currsum + item
                if newsum <= target and item >= comb[-1]:
                    combs.append((comb + [item], newsum))
        return op