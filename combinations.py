class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[i] for i in range(1, n + 1)]
        i = 0
        while i < len(combs):
            curr = combs[i]
            if len(curr) < k:
                for j in range(curr[-1] + 1, n + 1):
                    combs.append(curr + [j])
            i += 1
        return [comb for comb in combs if len(comb) == k]