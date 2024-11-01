class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        s = sum(skill)
        if s % (n // 2) != 0:
            return -1
        s //= (n // 2)
        res = 0
        ctr = Counter(skill)
        for el in ctr:
            if 2 * el < s:
                if ctr[el] != ctr[s - el]:
                    return -1
                res += el * (s - el) * ctr[el]
        if s % 2 == 0:
            if ctr[s // 2] & 1:
                return -1
            res += (ctr[s // 2] // 2) * (s // 2) ** 2
        return res