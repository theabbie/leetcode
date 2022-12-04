class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        total = sum(skill)
        if total % (n // 2) != 0:
            return -1
        k = total // (n // 2)
        res = 0
        i = 0
        j = n - 1
        pos = True
        while i < j:
            if skill[i] + skill[j] != k:
                pos = False
            res += skill[i] * skill[j]
            i += 1
            j -= 1
        if not pos:
            return -1
        return res